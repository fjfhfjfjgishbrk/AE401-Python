from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import datetime

now = datetime.datetime.now()
dateNow = now.strftime("%Y-%m-%d")
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://tw.eztable.com/search?country=tw&date=" + dateNow + "&people=2&searchTab=restaurant&source=mobile.eztable.com")
time.sleep(1)
for i in range(5):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)
pageSource = chrome.page_source
soup = BeautifulSoup(pageSource, "html.parser")
restaurants = soup.find_all("h4", class_="sc-gpHHfC")
price = soup.find_all("span", class_="sc-gPzReC")
space = soup.find_all("div", class_="sc-bEjcJn")
print("-------------------------------------------------------")
for i in range(len(restaurants)):
    if space[i].find("div").text == "No available tables under selected date.":
        continue
    else:
        availableTime = space[i].find_all("div")[1:4]
        print(restaurants[i].text, price[i].text)
        for j in availableTime:
            print(j.text, end=" ")
        print()
    print("-------------------------------------------------------")
chrome.close()