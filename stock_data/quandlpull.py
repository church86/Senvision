import pandas as pd
import os
import quandl
import time

auth_tok = "sJ1-JesK6dU83RFsYBkF"

<<<<<<< HEAD
#print (type(data))
data_intel = quandl.get("WIKI/INTC", trim_start = "2016-07-01", trim_end = "2017-5-30", authtoken=auth_tok)
f = open("alldata/Intel.csv", 'w')
data_intel.to_csv('alldata/Intel.csv', header=True, index=True, sep=',')

data_apple = quandl.get("WIKI/AAPL", trim_start = "2016-07-01", trim_end = "2017-5-30", authtoken=auth_tok)
f = open("alldata/Apple.csv", 'w')
data_apple.to_csv('alldata/Apple.csv', header=True, index=True, sep=",")

data_boeing = quandl.get("WIKI/BA", trim_start = "2016-07-01", trim_end = "2017-5-30", authtoken=auth_tok)
f = open("alldata/Boeing.csv", 'w')
data_boeing.to_csv('alldata/Boeing.csv', header=True, index=True, sep=",")

data_google = quandl.get("WIKI/GOOGL", trim_start = "2016-07-01", trim_end = "2017-5-30", authtoken=auth_tok)
f = open("alldata/Google.csv", 'w')
data_google.to_csv('alldata/Google.csv', header=True, index=True, sep=",")

data_jpmorganchase = quandl.get("WIKI/JPM", trim_start = "2016-07-01", trim_end = "2017-5-30", authtoken=auth_tok)
f = open("alldata/JPMorganChase.csv", 'w')
data_jpmorganchase.to_csv('alldata/JPMorganChase.csv', header=True, index=True, sep=",")

data_merck = quandl.get("WIKI/MRK", trim_start = "2016-07-01", trim_end = "2017-5-30", authtoken=auth_tok)
f = open("alldata/Merck.csv", 'w')
data_merck.to_csv('alldata/Merck.csv', header=True, index=True, sep=",")

data_png = quandl.get("WIKI/PG", trim_start = "2016-07-01", trim_end = "2017-5-30", authtoken=auth_tok)
f = open("alldata/Procter&Gamble.csv", 'w')
data_png.to_csv('alldata/Procter&Gamble.csv', header=True, index=True, sep=",")

data_walmart = quandl.get("WIKI/WMT", trim_start = "2016-07-01", trim_end = "2017-5-30", authtoken=auth_tok)
f = open("alldata/Walmart.csv", 'w')
data_walmart.to_csv('alldata/Walmart.csv', header=True, index=True, sep=",")
=======
#position of Tickername and company name must always be the same, dictionary of names made from these two arrays
TickerNames=["INTC","AAPL","BA","GOOGL","JPM","MRK","PG","WMT"]
CompNames=["Intel","Apple","Boeing","Google","JPMorganChase","Merck","Procter&Gamble","Walmart"]


ticker2Comp={}
for i in range(len(TickerNames)):
	ticker2Comp[TickerNames[i]]=CompNames[i]

>>>>>>> a74ce12f9bbc2e7a69a885f6944a43ea898ba180

#Pulls data from Quandl
for i in TickerNames:
	print "WIKI/"+str(i)
	data_intel = quandl.get("WIKI/"+str(i),trim_start = "2016-07-01", trim_end = "2017-3-30", authtoken=auth_tok)
	data_intel.to_csv("alldata/"+str(ticker2Comp[i])+'.csv', header=True, index=True, sep=',')