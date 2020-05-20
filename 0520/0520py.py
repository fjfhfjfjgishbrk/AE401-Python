import requests
import pytube
from bs4 import BeautifulSoup

r = requests.get("https://www.youtube.com/feed/trending")
soup = BeautifulSoup(r.text, "html.parser")

video = soup.find_all("div", class_="yt-lockup-content")
for i in range(6):
    if i == 2:
        continue
    videoLink = "https://www.youtube.com" + video[i].find("a")["href"]
    yt = pytube.YouTube(videoLink).streams[0].download(filename_prefix=str(i+1))
    print(str(i+1))

"""
video = soup.find_all("div", class_="yt-lockup-content")
imgDiv = soup.find_all("div", class_="yt-thumb video-thumb")
for i in range(10):
    title = video[i].find("a").text
    title = title.replace("|", "")
    img = imgDiv[i].find("img")["src"]
    if img[-3:] == "gif":
        img = imgDiv[i].find('img')['data-thumb']
    imgRes = requests.get(img)
    file = open("{}{}.jpg".format(str(i+1), title), "bw")
    file.write(imgRes.content)
"""


