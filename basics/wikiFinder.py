from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, features="lxml")
for link in bsObj.findAll('a'):
    if 'href' in link.attrs:
        with open("link.txt", 'a') as file:
            file.write(f"{link.attrs['href']} \n")
