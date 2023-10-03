# Beautiful find() and findAll() are the two functions likely use the most.

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features="html.parser")

# nameList = bsObj.find_all("span", {"class": "green"})
# for name in nameList:
# print(name.get_text())


# nameList = bsObj.findAll(string="the prince")
# print(len(nameList))

allText = bsObj.findAll(id="text")
# This line will through erorr due to nonstandard use of class in python class is reserve word.
# allText = bsObj.findAll(class="text")
# This line will not gonna through error
# allText = bsObj.findAll(class_="green")
with open("out.txt", 'w') as file:
    file.write(allText[0].get_text())
