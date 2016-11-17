import codecs
import os
import time
from eventregistry import *
from datetime import date, timedelta as td

CompanyNames=["Merck","Procter_&_Gamble","Walmart","Boeing","JPMorgan_Chase","Google","INTC","Apple"]

print "must be run inside the folder \"NewsFetcher\""


def getArticlesUrls(queryterm,startdate,enddate):
	companyfolderpath="../Urls/"+queryterm
	writefilepath=companyfolderpath+"/"+queryterm+"_"+str(startdate)+"_Urls.txt"
	if(os.path.isfile(writefilepath)): #checks if file exists. If it does, exit function
		print "skipping "+ queryterm+ " "+str(startdate)
		return
	print "running " +queryterm+ " " +str(startdate)
	er = EventRegistry()
	q = QueryArticles(lang=["eng"],isDuplicateFilter="skipDuplicates",hasDuplicateFilter="skipHasDuplicates")
	if not os.path.exists(companyfolderpath): #checks if folder exists. If not, make it
		os.makedirs(companyfolderpath)
		print "created" + companyfolderpath
	#set the date limit of interest
	q.setDateLimit(startdate, enddate)
	# find articles mentioning the company Apple		
	q.addConcept(er.getConceptUri(queryterm))
	# return the list of top 30 articles, including the concepts, categories and article image
	q.addRequestedResult(RequestArticlesUrlList(page=1,count=150))
	writefile=open(companyfolderpath+"/"+queryterm+"_"+str(startdate)+"_Urls.txt",'w')
	try:	
		results=er.execQuery(q)
		#print str(results)
		dict=results
		for url in dict['urlList']['results']:
			writefile.write(url.encode('utf-8') + "\n") #writes url by line to file
		print("# of Urls: " + str(len(dict['urlList']['results'])))
		writefile.close()
		time.sleep(1)
	except:
		


def iterateDays(startyear,startmonth,startdate,endyear,endmonth,enddate):#runs getArticlesUrls over range of dates


	d1 = date(startyear, startmonth, startdate)
	d2 = date(endyear, endmonth, enddate)

	delta = d2 - d1
	
	for i in range(delta.days + 1):
		currentDate= d1 + td(days=i)
		nextDate=d1+td(days=i+1)
		for company in CompanyNames:
			getArticlesUrls(company,currentDate,nextDate)
			
now= datetime.datetime.now()
now-td(days=1)

iterateDays(2016,9,5,now.year,now.month,now.day)
		 
#getArticlesUrls("Apple",date(2016,9,15),date(2016,9,16))	
