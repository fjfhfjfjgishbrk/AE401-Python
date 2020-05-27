from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone")
time.sleep(3)
for i in range(5):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)
pageSource = chrome.page_source
soup = BeautifulSoup(pageSource, "html.parser")
items = soup.find("div", class_="Cm_C").find_all("dl")
for item in items:
    print(item.find_all("a")[1].text)
chrome.close()
