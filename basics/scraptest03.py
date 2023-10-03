from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, features="lxml")

# This loop will print children of table group whose id is gfitlist
# for child in bsObj.find("table", {"id": "giftlist"}).children:
#    print(child)

# There are several little functions in BeutifulSoup that will help in scraping

# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#    print(sibling)

# print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"
#                          }).parent.previous_sibling.get_text())
output = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
print(output)
