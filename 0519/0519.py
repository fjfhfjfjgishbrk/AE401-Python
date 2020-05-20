import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.books.com.tw/web/sys_saletopb/books/02?attribute=30&loc=act_menu_th_46_002")
soup = BeautifulSoup(r.text)
divs = soup.find_all(class_="type02_bd-a")
c = 1
for book in divs:
    bookName = book.find('a').text
    authorName = book.find_all('a')[1].text
    bookPrice = book.find_all('b')[-1].text
    print("Number {}: {}, Author: {}, Price: {}$".format(c, bookName, authorName, bookPrice))
    c += 1
