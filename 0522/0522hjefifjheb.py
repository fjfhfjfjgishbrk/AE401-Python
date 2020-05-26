import requests
from bs4 import BeautifulSoup
payload = {"startStation": "977abb69-413a-4ccf-a109-0272c24fd490",
           "endStation": "3301e395-46b8-47aa-aa37-139e15708779",
           "theDay": "2020/06/10",
           "timeSelect": "18:00",
           "waySelect": "DepartureInMandarin"}
res = requests.post("https://m.thsrc.com.tw/tw/TimeTable/SearchResultList",data = payload)

soup = BeautifulSoup(res.text,"html.parser")
print(soup)
"""
for i in range(1,11):
    trainNumber = soup.find_all('div',class_="ui-block-a")[i]
    trainTime = soup.find_all('div',class_="ui-block-b")[i]
    nonReservedNumber = soup.find_all('div',class_="ui-block-c")[i]
    print("車次:"+trainNumber.text)
    print("出發-抵達(行車時間):"+trainTime.text)
    print("自由座車廂數:"+nonReservedNumber.text)
    print("=====================================================")
"""
