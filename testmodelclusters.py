import os
import csv
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

allvalues = {}

#company_name = raw_input("Enter company name: ")

##########################################################
# open files containing words ############################
##########################################################

good_words = open("Vocab/good_words", "r")
bad_words =  open("Vocab/bad_words", "r")
neutral_words = open("Vocab/neutral_words", "r")
good_for_neutral = open("Vocab/good_for_neutral", "r") 
bad_for_neutral = open("Vocab/bad_for_neutral", "r")

good_clusters = open("Vocab_Clusters/good_words_clustered.txt", "r")
bad_clusters = open("Vocab_Clusters/bad_words_clustered.txt", "r")
neutral_good_clusters = open("Vocab_Clusters/good_for_neutral_clustered.txt", "r")
neutral_bad_clusters = open("Vocab_Clusters/bad_for_neutral_clustered.txt", "r")

###########################################################
#append all the words and their contexts to various arrays# 
###########################################################
good_arr = []
bad_arr = []
neutral_arr = []
good_for_neutral_arr = []
bad_for_neutral_arr = []

good_clusters_arr = []
bad_clusters_arr = []
neutral_good_clusters_arr = []
neutral_bad_clusters_arr = []


##############################################
# READING INDIVIDUAL WORDS ###################
##############################################
reader = csv.reader(good_words, delimiter=" ")
for row in reader:
	good_arr.append(row)
reader = csv.reader(bad_words, delimiter = " ")
for row in reader:
	bad_arr.append(row)
reader = csv.reader(neutral_words, delimiter = " ")
for row in reader:
	neutral_arr.append(row)
reader = csv.reader(good_for_neutral, delimiter= " ")
for row in reader:
	good_for_neutral_arr.append(row)
reader = csv.reader(bad_for_neutral, delimiter = " ")
for row in reader:
	bad_for_neutral_arr.append(row)

##############################################
###            READING CLUSTERS            ###
##############################################
reader = csv.reader(good_clusters, delimiter = " ")
for row in reader:
	good_clusters_arr.append(row)
reader = csv.reader(bad_clusters, delimiter = " ")
for row in reader:
	bad_clusters_arr.append(row)
reader = csv.reader(neutral_good_clusters, delimiter = " ")
for row in reader:
	neutral_good_clusters_arr.append(row)
reader = csv.reader(neutral_bad_clusters, delimiter = " ")
for row in reader:
	neutral_bad_clusters_arr.append(row)


class MySentences(object):
	def __init__ (self,dirname):
		self.dirname = dirname
	def __iter__ (self):
		for fname in os.listdir(self.dirname):
			for line in open(os.path.join(self.dirname,fname)):
				yield line.split()


######################################################################################################
###                            COMPANY_NAMES AND DATE COLLECTION                                   ###
######################################################################################################
full_company_names = ['Apple', 'Boeing', 'Google', 'Intel', 'Merck', 'Morgan Chase', 'p&g', 'Walmart']
#full_company_names = open("file_containing_company_names.txt", "r")
dates = []
current_year = raw_input("Enter current year: ")
current_month = raw_input("Enter current month: ")
firstdate = raw_input("Enter start date (put a 0 on front if single digit): ")
lastdate = raw_input("Enter end date: ")

for i in range (int(firstdate), int(lastdate)+1):
	if len(str(i)) == 1:
		dates.append(str(current_year) + "-" + str(current_month) + "-0" + str(i))
	else:
		dates.append(str(current_year) + "-" + str(current_month) + "-" + str(i))


##########################################################################################
###                         loop through all the companies                             ### 
##########################################################################################
for company_name in full_company_names:

	outf = open('./descriptors/' + str(company_name) + "_descriptor" + ".txt", 'w')
	outf.write('Word' + "\t")
	for x in good_words:
		outf.write(str(x) + "\t")
	for y in bad_words:
		outf.write(str(y) + "\t")
	outf.write("\n")


	for date in dates:

		outf.write(str(date) + "\t")

		num_features = 40 #subject to change
		min_word_count = 1 #subject to change
		num_workers = 15 #should be good
		context = 10 #subject to change
		#downsampling = 1e-3

		sentences = LineSentence('/Tweets/' + company_name + '/'  + company_name + '_' + date + 'Tweets.txt')
		print("Training model...")
		model = word2vec.Word2Vec(sentences, workers=num_workers, size=num_features, min_count=min_word_count, window=context)

		posarr = []
		negarr = []

		for x in good_words:
			try:
				dist = model.similarity(str(company_name), x)
				posarr.append(dist)
				allvalues[str(company_name) + "_" + str(x)] = dist
			except KeyError:
				posarr.append(0)
				allvalues[str(company_name) + "_" + str(x)] = 0
				continue
 
		for x in bad_words:
			try:
				dist = model.similarity(str(company_name), x) 
				negarr.append(dist)
				allvalues[str(company_name) + "_" + str(x)] = dist 
			except KeyError:
				negarr.append('N/A')
				allvalues[str(company_name) + "_" + str(x)] = 0
				continue

		for x in neutral_words:
			for y in good_for_neutral:
				try:
					dist = model.similarity(str(x), str(y))
					allvalues[str(x) + "_" + str(y)] = dist
				except KeyError:
					allvalues[str(x) + "_" + str(y)] = 0


			for y in bad_for_neutral:
                                        dist = model.similarity(str(x), str(y))
                                        allvalues[str(x) + "_" + str(y)] = dist
                                except KeyError:
                                        allvalues[str(x) + "_" + str(y)] = 0 




#		outf.write('MOST SIMILAR WORDS' + '\n')
#		simarr = model.most_similar(str(company_name))
#		for x in simarr:
#			try:
#				for y in x:
#					outf.write(str(y) + '\t')
#				outf.write('\n')
#			except UnicodeEncodeError:
#				continue
#
#		for distance in posarr:
#			outf.write(str(distance) + '\t')
#		for distance in negarr:
#			outf.write(str(distance) + '\t')
#		outf.write('\n')
