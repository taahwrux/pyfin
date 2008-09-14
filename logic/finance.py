import math

def ToPercent(dec):
    if dec > 1 or dec < 0:
        return dec
    else:
        return dec * 100


def DailyHPR(beg, end):
    hpr = (end / beg) - 1
    return hpr * 100

def GAverage(li):
    # find product of (1 + X1)(1+ X2).... (1 + Xn)
    if not isinstance(li, list):
        print "Not a list object"
        return
    
    prod = reduce(lambda x, y: (x+1)*(y+1), li)
    
    nrt = (1/float(len(li)))
    return math.pow(prod, nrt) - 1


if __name__ == "__main__":
    a = [.5, 1, .8, .5]
    print ToPercent(GAverage(a))

