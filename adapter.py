# this is a fetch module for getting historical price of stocks from Google Finance

import urllib
from container import DataContainer, DataEntry
from util import DateConv

# "http://finance.google.com/finance/historical?q=NYSE:IBM&output=csv"
class DataAdapter(object):
    def __init__(self):
        self.__mURL = ""
        self.__mData = None
        self.__mDict = dict()

    def getURL(self):
        return self.__mURL

    def setURL(self, url):
        self.__mURL = url
        
    url = property(getURL, setURL)

    def InsertItem(self, key, value):
        self.__mDict[key] = value

    def QueryItem(self, key):
        return self.__mDict[key]

    def Generate(self):
        self.__mDict
    	all = []
        for x in self.__mDict:
            all.append("%s=%s" % (x, self.__mDict[x]))
            
        return self.url + "&".join(all)

    def Fetch(self):
        """this function will return DataContainer object""" 
        s = self.Generate()
        f = urllib.urlopen(s)
        data = f.read()
        f.close()
        
        entries = data.split('\n')[1:-1]
        con = DataContainer()

        for entry in entries:
            # parse entry to standard 
            temp = DataEntry()
            datestr, temp.open, temp.high, temp.low, temp.close, temp.volume = entry.split(',')
            temp.date = DateConv.ToDateObject(datestr)
            con.InsertEntry(temp)

        return con


        
        
    
    
if __name__ == "__main__":
    gFin = DataAdapter()
    gFin.url = "http://finance.google.com/finance/historical?"
    gFin.InsertItem('q', 'NYSE:IBM')
    gFin.InsertItem('output', 'csv')
    con = gFin.Fetch()
    con.ListAll() 
