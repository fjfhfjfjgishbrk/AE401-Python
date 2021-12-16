import requests
from bs4 import BeautifulSoup
from builtins import str
import json
import re
import urllib
import statistics
from time import sleep
import numpy as np
import xlsxwriter


def most_frequent(List):
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return (itm)


def reject_outliers(data, m=1.7):
    return data[abs(data - np.mean(data)) < m * np.std(data)]


cardList = ['cpz1 jp019', 'st13 jpv01', 'st13 jp042', 'ysd6 jp041', 'sd28 jp043', 'gs04 jp009', 'gdb1 jp050', 'st13 jpv09',
            'ysd6 jp042', 'dp13 jp019', 'dp14 jp019', 'prio jp058', 'sd25 jp004', 'sr02 jp037']
workSheetData = []
c = 1

for card in cardList:
    keyList = card.replace(' ', '-')
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
        'x-api-source': 'pc',
        'referer': f'https://shopee.tw/search?keyword={urllib.parse.quote(card)}'
    }

    s = requests.Session()
    url = 'https://shopee.tw/api/v4/search/product_labels'
    r = s.get(url, headers=headers)

    base_url = 'https://shopee.tw/api/v2/search_items/'
    query = f"by=relevancy&keyword={card}&limit=50&newest=0&order=desc&page_type=search&version=2"
    url = base_url + '?' + query
    r = s.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        data = r.json()

    for i in data.items():
        if i[0] == "items":
            sellItems = i[1]

    totalPrice = 0
    totalCount = 0
    nameList = []
    priceList = []

    for i in sellItems:
        itemName = i['name']
        itemPrice = round(i['price'] / 100000)
        if keyList.lower() in itemName.lower():
            itemSplit = re.split(' |]|\)|\(|】|］', itemName.lower())
            #print(itemName, itemPrice)
            if keyList.lower() in itemSplit:
                appendIndex = itemSplit.index(keyList.lower())
                while True:
                    appendIndex += 1
                    if len(itemSplit) > appendIndex:
                        if "-" in itemSplit[appendIndex] or itemSplit[appendIndex] == '':
                            continue
                        nameList.append(itemSplit[appendIndex])
                    else:
                        break
            totalPrice += itemPrice
            priceList.append(itemPrice)
            totalCount += 1

    numpyPrice = np.array(priceList)
    if numpyPrice.size > 3:
        numpyPrice = reject_outliers(numpyPrice)

    if numpyPrice.size > 0:
        #print("-------------------------------------------")
        print("Card %d / %d" % (c, len(cardList)))
        print(most_frequent(nameList))
        print("Average %d$, Max: %d$, Q3: %d$, Median %d$, Q1: %d$, Min %d$" % (np.average(numpyPrice), numpyPrice.max(), np.percentile(numpyPrice, 75), np.median(numpyPrice), np.percentile(numpyPrice, 25), numpyPrice.min()))
        print("-------------------------------------------")
        workSheetData.append([most_frequent(nameList), np.round(np.average(numpyPrice)), np.round(numpyPrice.max()), np.round(np.percentile(numpyPrice, 75)),
                              np.round(np.median(numpyPrice)), np.round(np.percentile(numpyPrice, 25)), np.round(numpyPrice.min())])

    c += 1
    sleep(3)

workbook = xlsxwriter.Workbook('card price.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, "Card name")
worksheet.write(0, 1, "Average")
worksheet.write(0, 2, "Max")
worksheet.write(0, 3, "Q3")
worksheet.write(0, 4, "Median")
worksheet.write(0, 5, "Q1")
worksheet.write(0, 6, "Min")

row = 1
col = 0

for card in workSheetData:
    for i in range(len(card)):
        worksheet.write(row, col + i, card[i])
    row += 1

workbook.close()