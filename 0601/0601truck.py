from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, VideoSendMessage
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time


bot = LineBotApi("SO3U/GpBN0KYGAdsrT/NEGh9lQ8q7SCb1rj/ajDhWsYNyC2uHEPvRWzFaXUgeDVoj0k6tCFjFERXUUfcJozzIG88dGLmpBK8WR6PE+xSLneu+wuebE3mgQRt4WZ1LRAgr3RrGv+n3jlNPIYgeT2euQdB04t89/1O/w1cDnyilFU=")
userID = 'U828989e3a59614b66e4262c62f480c6f'

chrome = webdriver.Chrome()
chrome.get("https://www.lihpaoresort.com/LihpaolandApp")
time.sleep(1)
soup = BeautifulSoup(chrome.page_source, "html.parser")
logo = "https://www.lihpaoresort.com" + soup.find("h1", class_="logo").find("img")['src']
video = soup.find("div", class_="video").find("a")['href'].strip()
chrome.find_element_by_class_name("guide-4").click()
time.sleep(1)

chrome.find_elements_by_class_name("item")[4].find_element_by_class_name("view").click()
time.sleep(1)

soup = BeautifulSoup(chrome.page_source, "html.parser")
ticketName = soup.find("h3", class_="ticket-name").text[3:]
price = "特價" + soup.find("strong", class_="price-sale").text
buyUrl = chrome.current_url
chrome.back()
chrome.back()
time.sleep(1)

chrome.find_element_by_class_name("guide-2").click()
time.sleep(1)

soup = BeautifulSoup(chrome.page_source, "html.parser")
openTime = soup.find("div", class_="fix-content").find_all("div", class_="fix-row1")[2].text.strip()[2:]
chrome.back()
time.sleep(1)

chrome.find_element_by_class_name("guide-3").click()
time.sleep(1)

soup = BeautifulSoup(chrome.page_source, "html.parser")
travelPic = "https://www.lihpaoresort.com/LihpaolandApp" + soup.find("div", class_="describe").find_all("img")[6]['src'][2:]

chrome.close()

location = (24.323074, 120.695524)

logoMessage = ImageSendMessage(original_content_url=logo, preview_image_url=logo)
videoMessage = TextSendMessage(text=video)
openInfoMessage = TextSendMessage(text=openTime)
buyLinkMessage = TextSendMessage(text=buyUrl)
firstSendMessages = [logoMessage, videoMessage, openInfoMessage, buyLinkMessage]
bot.push_message(userID, firstSendMessages)
time.sleep(5)
ticketInfoMessage = TextSendMessage(text=ticketName)
priceMessage = TextSendMessage(text=price)
travelMessage = ImageSendMessage(original_content_url=travelPic, preview_image_url=travelPic)
positionMessage = LocationSendMessage(title="麗寶樂園", address="台中市后里區福容路8號", latitude=location[0], longitude=location[1])
secondSendMessages = [ticketInfoMessage, priceMessage, travelMessage, positionMessage]
bot.push_message(userID, secondSendMessages)

