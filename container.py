import datetime

class DataContainer(object):
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
        self.__mDate = date
    date = property(getDate, setDate)


if __name__ == "__main__":
    x = DataContainer()
    x.date = 123
    print x.date
