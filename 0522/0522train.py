import requests
from bs4 import BeautifulSoup
import re

res = requests.get("https://m.thsrc.com.tw/tw/TimeTable/SearchResult")
soup = BeautifulSoup(res.text, "html.parser")

stationList = soup.find('select', id="startStation").find_all("option")
stationDict = {}
for i in range(1, len(stationList)):
    stationDict[stationList[i].text.strip()] = stationList[i]["value"]


def getStation(text):
    retValue = input(text)
    if retValue in stationDict:
        return retValue
    else:
        print("Invalid station")
        return getStation(text)


stationFrom = getStation("From: ")
stationTo = getStation("To: ")
day = input("Date: ")
time = input("Time: ")


def getTimeTable(t):
    finish = False
    payload = {"startStation": stationDict[stationFrom],
               "endStation": stationDict[stationTo],
               "theDay": day,
               "timeSelect": t,
               "waySelect": "DepartureInMandarin"}
    postData = requests.post("https://m.thsrc.com.tw/tw/TimeTable/SearchResultList", data=payload)
    soup = BeautifulSoup(postData.text, "html.parser")
    for i in range(1, 11):
        trainNumber = soup.find_all('div', class_="ui-block-a")[i]
        trainTime = soup.find_all('div', class_="ui-block-b")[i]
        nonReservedNumber = soup.find_all('div', class_="ui-block-c")[i]
        if re.match("[0-9]{4}", trainNumber.text) is None:
            finish = True
            break
        print("車次: " + trainNumber.text)
        print("出發-抵達(行車時間): " + trainTime.text)
        print("自由座車廂數: " + nonReservedNumber.text)
        print("=====================================================")
    if finish:
        print("Done")
    else:
        nextTime = soup.find_all('div', class_="ui-block-b")[10].text[:5]
        nextTime = nextTime[:3] + str(int(nextTime[3:5]) + 1)
        getTimeTable(nextTime)


print("=====================================================")
getTimeTable(time)