from container import DataEntry, DataContainer
from logic.finance import DailyHPR

class DataAnalyzer(object):
    def __init__(self):
        # DataContainer object
        self.__mSrc = DataContainer()
    
    def getSrc(self):
        return self.__mSrc
    def setSrc(self, src):
        self.__mSrc = src
    src = property(getSrc, setSrc)


