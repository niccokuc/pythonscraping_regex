import urllib.request
import re

urls = ["http://google.com",
        "http://nytimes.com",
        "http://CNN.com",
        "http://lifestylerhythmsfitness.com.au",
        "http://seek.com"]
i=0
regex = ('<title>(.+?)</title>')
pattern = re.compile(regex)

while i<len(urls):
    htmlfile = urllib.request.urlopen(urls[i])
    htmltext = str(htmlfile.read())
    titles = pattern.findall(str(htmltext))
    print(titles)
    i += 1