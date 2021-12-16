import requests
from bs4 import BeautifulSoup

number = 122345

res = requests.get("https://nhentai.net/g/" + str(number) + "/")
soup = BeautifulSoup(res.text, "html.parser")
tagType = soup.find_all("span", {"class": "tags"})
allTagName = soup.find_all("span", {"class": "name"})
title = soup.find_all("span", {"class": "pretty"})
tagName = ["Parodies", "Characters", "Tags", "Artists", "Groups", "Languages", "Categories", "Pages"]
outTitle = []
for i in title:
    outTitle.append(i.string)
if len(tagType) != 0:
    tagTypeNum = []
    for i in tagType:
        tagTypeNum.append(int(str(i).count("tag-")))
    tagTypeNum.pop()
    tagTypeNum.pop()
    out = []
    count = 0
    for i in tagTypeNum:
        temp = []
        for j in range(i):
            temp.append(allTagName[count].string)
            count += 1
        out.append(temp)
    print("Title:", " / ".join(outTitle))
    for i in range(len(out)):
        print("{:s}: {:s}".format(tagName[i], " / ".join(out[i])))
else:
    print("No hentai found")
