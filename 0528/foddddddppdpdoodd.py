from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import datetime
import requests

now = datetime.datetime.now()
dateNow = now.strftime("%Y-%m-%d")
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://tw.eztable.com/search?country=tw&date=2020-05-30&people=2&q=%E4%B8%80%E8%B5%B7%E5%B0%8F%E9%A3%9F%E9%A4%A8&searchTab=restaurant&source=mobile.eztable.com&utm_campaign=branding_keyword&utm_medium=cpc&utm_source=marketing")
time.sleep(2)
#for i in range(5):
    #chrome.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    #time.sleep(1)
pageSource = chrome.page_source
soup = BeautifulSoup(pageSource, "html.parser")
space = soup.find_all("div", class_="sc-gzVnrw")
restaurants = soup.find_all("h4", class_="sc-gpHHfC")
value1 = restaurants[0].text + " Time: " + space[0].text
chrome.find_elements_by_class_name("sc-fgfRvd")[0].click()
time.sleep(2)
pageSource = chrome.page_source
soup = BeautifulSoup(pageSource, "html.parser")
image = soup.find_all("div", class_="sc-ESoVU")[0]['style']
img_url = image.split("\"")[1]
chrome.back()
time.sleep(2)
chrome.find_elements_by_class_name("sc-gzVnrw")[0].click()
time.sleep(5)
pageSource = chrome.page_source
soup = BeautifulSoup(pageSource, "html.parser")
people = soup.find_all("div", class_="sc-keVrkP")
value1 += "  " + people[0].text.split(",")[1].strip()
chrome.find_elements_by_class_name("sc-fHxwqH")[0].click()
webhook_key = "PI8b5ouDPVMzfDrEQlHyP"
trigger_name = "abc"
url = 'https://maker.ifttt.com/trigger/'+trigger_name+'/with/key/'+webhook_key+'?value1=' + value1 + "&value2=" + img_url
requests.get(url)
chrome.close()