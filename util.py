# date conversion
import datetime

class DateConv(object):
    def ToDateObject(str):
        __month = {
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

        temp = str.split('-')
        temp.reverse()
        year, month, date = temp
        # YY to YYYY
        year_int = int("20" + year)
        month_int = __month[month]

        return datetime.date(year_int, month_int, int(date))
    ToDateObject = staticmethod(ToDateObject)

if __name__ == "__main__":
    y = DateConv.ToDateObject('12-Sep-08')
    print y.isoformat()
