import urllib.request, re

symbolfile = open("symbolfile.txt")
symbolslist = symbolfile.read()
symbolslist = symbolslist.split("\n")
print(symbolslist[0])
j = 0
while j<len(symbolslist):
    url = "http://finance.yahoo.com/q?s="+symbolslist[j]+"&ql=1"
    regex = ('<span id="yfs_l84[^.]*">(.+?)</span>')
    pattern = re.compile(regex)
    htmlfile = urllib.request.urlopen(url)
    htmltext = str(htmlfile.read())
    prices = pattern.findall(str(htmltext))
    print("The prices are: ", prices, symbolslist[j])
    j += 1