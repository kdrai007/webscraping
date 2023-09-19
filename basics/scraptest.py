# from urllib.request import urlopen
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
# html = urlopen("http://pythonscraping.com/pages/page1.html")
# adding additonal corrector by passing argument features
# bsObj = BeautifulSoup(html.read(), features="html.parser")
# print(bsObj.h1)
# this can be written in programmatically like uisng try and Exception


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features="html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://pythonscraping.com/pages/page1.html")
if title is None:
    print("Title could not be found")
else:
    print(title)
