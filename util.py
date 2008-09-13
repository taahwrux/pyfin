# date conversion
import datetime

class DateConv(object):
    def __init__(self):
        self.__month = {
            'Jan':1,
            'Feb':2,
            'Mar':3,
            'Apr':4,
            'May':5,
            'Jun':6,
            'Jul':7,
            'Aug':8,
            'Sep':9,
            'Oct':10,
            'Nov':11,
            'Dec':12}

    def ToDateObject(self, str):
        """12-Sep-2008"""
        temp = str.split('-')
        temp.reverse()
        year, month, date = temp
        month_int = self.__month[month]
        return datetime.date(int(year), month_int, int(date))

if __name__ == "__main__":
    x = DateConv()
    y = x.ToDateObject('12-Sep-2008')
    print y.isoformat()
