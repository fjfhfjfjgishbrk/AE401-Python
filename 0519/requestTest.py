import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
soup = BeautifulSoup(r.text,"html.parser")
sel = soup.select("div.title a")
for s in sel:
    print(s["href"], s.text)