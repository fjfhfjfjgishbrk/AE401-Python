#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:06:24 2020

@author: fdbfvuie
"""

"""
內容
我國的身分證字號有底下這樣的規則，因此對於任意輸入的身分證字號可以有一些基本的判斷原則，請您來判斷一個身分證字號是否是正常的號碼(不代表確有此號、此人)。

(1) 英文代號以下表轉換成數字

      A=10 台北市     J=18 新竹縣     S=26 高雄縣
      B=11 台中市     K=19 苗栗縣     T=27 屏東縣
      C=12 基隆市     L=20 台中縣     U=28 花蓮縣
      D=13 台南市     M=21 南投縣     V=29 台東縣
      E=14 高雄市     N=22 彰化縣     W=32 金門縣
      F=15 台北縣     O=35 新竹市     X=30 澎湖縣
      G=16 宜蘭縣     P=23 雲林縣     Y=31 陽明山
      H=17 桃園縣     Q=24 嘉義縣     Z=33 連江縣
      I=34 嘉義市     R=25 台南縣

  (2) 英文轉成的數字, 個位數乘９再加上十位數的數字

  (3) 各數字從右到左依次乘１、２、３、４．．．．８

  (4) 求出(2),(3) 及最後一碼的和

  (5) (4)除10 若整除，則為 real，否則為 fake

 例： T112663836

2 + 7*9 + 1*8 + 1*7 + 2*6 + 6*5 + 6*4 + 3*3 + 8*2 + 3*1 + 6 = 180

除以 10 整除，因此為 real 
"""

dic = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", "H": "17", "I": "34", "J": "18", "K": "19",\
       "L": "20", "M": "21", "N": "22", "O": "35", "P": "23", "Q": "24", "R": "25", "S": "26", "T": "27", "U": "28" ,"V": "29",\
       "W": "32", "X": "30", "Y": "31", "Z": "33"}
while True:
    try:
        n = input()
        numSum = int(dic[n[0]][0]) + int(dic[n[0]][1]) * 9
        for i in range(1, 9):
            numSum += int(n[i]) * (9 - i)
        numSum += int(n[9])
        if numSum % 10 == 0:
            print("real")
        else:
            print("fake")
    except:
        break