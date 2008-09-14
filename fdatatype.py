# FDataType

from logic.finance import ToPercent as topercent
class FFloat(float):
    def __init__(self, num):
        self.__mFloat = num

    def ToPercent(self):
        return topercent(self.__mFloat)
        

class FPrice(float):
    def __init__(self, thePrice):
        pass

class FCurrency(FPrice):
    def __init__(self):
        pass





if __name__ == "__main__":
    x = FObject(.3654)
    print x.ToPercent()
    

