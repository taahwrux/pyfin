import datetime

class DataEntry(object):
    def __init__(self):
        self.__mDate = None
        self.__mOpen = None
        self.__mHigh = None
        self.__mLow = None
        self.__mClose = None
        self.__Volume = None

    # Date
    def getDate(self):
        return self.__mDate
    def setDate(self, date):
        if isinstance(date, datetime.date):
            self.__mDate = date
    date = property(getDate, setDate)

    # Open
    def getOpen(self):
        return self.__mOpen
    def setOpen(self, open):
        self.__mOpen = open
    open = property(getOpen, setOpen)

    # High
    def getHigh(self):
        return self.__mHigh
    def setHigh(self, high):
        self.__mHigh = high
    high = property(getHigh, setHigh)

    # Low
    def getLow(self):
        return self.__mLow
    def setLow(self, low):
        self.__mLow = low
    low = property(getLow, setLow)

    # Close
    def getClose(self):
        return self.__mClose
    def setClose(self, close):
        self.__mClose = close
    close = property(getClose, setClose)

    # Volume
    def getVolume(self):
        return self.__mVolume
    def setVolume(self, volume):
        self.__mVolume = volume
    volume = property(getVolume, setVolume)


class DataContainer(object):
    def __init__(self):
        self.__mEntries = []
        self.__mTicker = ""

    def InsertEntry(self, entry):
        if isinstance(entry, DataEntry):
            self.__mEntries.append(entry)

    def ListAll(self):
        for entry in self.__mEntries:
            print entry.date, entry.open
if __name__ == "__main__":
    x = DataContainer()
    x.date = datetime.date(2008, 11, 1)
    print x.date
