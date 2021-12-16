from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import datetime

health = []
atk = []
defense = []


now = datetime.datetime.now()
dateNow = now.strftime("%Y-%m-%d")
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("https://genshin.honeyhunterworld.com/db/char/fischl/?lang=EN")
time.sleep(2)
pageSource = chrome.page_source
soup = BeautifulSoup(pageSource, "html.parser")
allStats = soup.find_all("div", class_="skilldmgwrapper")
asTr = allStats[0].find_all("tr")
for i in range(7):
    tagTr = asTr[i * 2 + 1]
    tdLook = tagTr.find_all("td")
    health.append(tdLook[1].getText())
    atk.append(tdLook[2].getText())
    defense.append(tdLook[3].getText())
tempStat = []
sixTr = asTr[6]
eightTr = asTr[8]
tdLookSix = sixTr.find_all("td")
tdLookEight = eightTr.find_all("td")
for i in range(3):
    tempStat.append(int(tdLookSix[i + 1].getText()))
    tempStat.append(int(tdLookEight[i + 1].getText()))

print("Health:", ", ".join(health))
print("Attack:", ", ".join(atk))
print("Defense:", ", ".join(defense))
print("Health growth:", str(round((tempStat[0] - int(health[2])) / 20 + (tempStat[1] - int(health[3])) / 20, 2)))
print("Attack growth:", str(round((tempStat[2] - int(atk[2])) / 20 + (tempStat[3] - int(atk[3])) / 20, 2)))
print("Defense growth:", str(round((tempStat[4] - int(defense[2])) / 20 + (tempStat[5] - int(defense[3])) / 20, 2)))

skillName = ["NA", "Skill", "Burst"]

for k in range(3):
    print(skillName[k])
    naStats = allStats[k + 1].find_all("tr")
    for i in range(len(naStats)):
        if i == 0:
            continue
        allTd = naStats[i].find_all("td")
        if "s" in allTd[1].getText():
            continue
        tempArray = []
        nameStat = []
        if "/" in allTd[0].getText():
            nameStat = allTd[0].getText().split("/")
            tempArray = [[], []]
        elif "+" in allTd[1].getText():
            nameStat.append(allTd[0].getText())
            tempArray = [[], []]
        else:
            nameStat.append(allTd[0].getText())
        for j in range(15):
            if len(nameStat) > 1:
                tdSplit = allTd[j + 1].getText().split("/")
                tempArray[0].append(tdSplit[0][:-1].replace("%", ""))
                tempArray[1].append(tdSplit[1][1:].replace("%", ""))
            elif "+" in allTd[j + 1].getText():
                tdSplit = allTd[j + 1].getText().split("+")
                a = tdSplit[0].index("%")
                tempArray[0].append(tdSplit[0][:a])
                tempArray[1].append(tdSplit[1][1:].replace("%", ""))
            else:
                tempArray.append(allTd[j + 1].getText().replace("%", ""))
        if len(nameStat) > 1:
            for j in range(len(nameStat)):
                print("\"%s\": [%s]," % (nameStat[j], ", ".join(tempArray[j])))
        else:
            if len(tempArray) == 2:
                print("\"%s\": [%s]," % (nameStat[0], ", ".join(tempArray[0])))
                print("\"Addtional\": [%s]," % ", ".join(tempArray[1]))
            else:
                print("\"%s\": [%s]," % (nameStat[0], ", ".join(tempArray)))

time.sleep(2)
chrome.quit()

