import urllib.request
import time

stockToPull = 'AAPL'

def pullData(stock):
    try:
        fileLine = stock+'.csv'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
        sourceCode = urllib.request.urlopen(urlToVisit).read()

        splitSource = sourceCode.splitlines()

        for eachLine in splitSource:
            eachLine = eachLine.decode('utf-8')
            splitLine = eachLine.split(',')
            saveFile = open(fileLine, 'a')
            if(len(splitLine) == 6):
                if 'value' not in eachLine:
                    #for eachToken in splitLine:
                    lineToWrite = eachLine+'\n'
                    saveFile.write(lineToWrite)
        saveFile.close()
        print('Pulled stock: '+stock)
        #time.sleep(5)
    except IOError as err:
        print('File Error:' + str(err))
   
pullData(stockToPull)
