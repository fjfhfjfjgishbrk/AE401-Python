import re
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.youtube.com/feed/trending")
soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all("a")
p = True
for link in links:
    if re.match("^/watch[?]v=", link['href']) != None and p == True:
        print("https://www.youtube.com" + link['href'])
        p = False
    else:
        p = True