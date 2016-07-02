import urllib.request, re
symbolslist = ["AAPL", "SPY", "GOOG", "NFLX"]
j = 0
while j<len(symbolslist):
    url = "http://finance.yahoo.com/q?s="+symbolslist[j]+"&ql=1"
    regex = ('<span id="yfs_l84_'+symbolslist[j].lower()+'">(.+?)</span>')
    pattern = re.compile(regex)
    htmlfile = urllib.request.urlopen(url)
    htmltext = str(htmlfile.read())
    prices = pattern.findall(str(htmltext))
    print("The price of ",symbolslist[j]," = ",prices[0])
    j += 1