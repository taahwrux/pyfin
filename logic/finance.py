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

    prod = 1
    for x in li:
        prod = prod * (x + 1)
    
    nrt = (1/float(len(li)))
    return math.pow(prod, nrt) - 1


if __name__ == "__main__":
    a = [-0.5, 1.0]
    print len(a)
    re = GAverage(a)
    print ToPercent(re)

    
