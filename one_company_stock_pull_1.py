import urllib.request
import time
import pandas as pd

stockToPull = 'AAPL'

def pullData(stock):
    fileLine = stock+'.csv'
    urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
    sourceCode = urllib.request.urlopen(urlToVisit).read()

    splitSource = sourceCode.splitlines()
    strLine = splitSource[0].decode('utf-8')
    strSplit = strLine.split('/')

    for eachLine in strSplit:
        print(eachLine)

pullData(stockToPull)    
