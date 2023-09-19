from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features="html.parser")

nameList = bsObj.find_all("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
