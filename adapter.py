# this is a fetch module for getting historical price of stocks from Google Finance

import urllib

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
        s = self.Generate()
        f = urllib.urlopen(s)
        data = f.read()
        f.close()
        print data
    
    

        
        
    
    
if __name__ == "__main__":
    gFin = DataAdapter()
    gFin.url = "http://finance.google.com/finance/historical?"
    gFin.InsertItem('q', 'NYSE:IBM')
    gFin.InsertItem('output', 'csv')
    gFin.Fetch()