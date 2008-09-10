# this is a fetch module for getting historical price of stocks from Google Finance

import urllib

add = "http://finance.google.com/finance/historical?q=NYSE:IBM&output=csv"

f = urllib.urlopen(add)
csv = f.read()

print csv

f.close()

