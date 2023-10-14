from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
currentDate = datetime.datetime.now()
random.seed(currentDate.timestamp())


def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# Reterive a list of all external links found in a page


def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # Find all links that starts with http or www on the page
    for link in bsObj.findAll("a", href=re.compile(
            "^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressPart = address.replace("https://", "").split("/")
    return addressPart


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, features="lxml")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj, startingPage)
        return getExternalLinks(bsObj,
                                internalLinks[random.randint(0, len(internalLinks-1))])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("random external link is: ", externalLink)
    followExternalOnly(externalLink)


followExternalOnly("http://oreilly.com")
