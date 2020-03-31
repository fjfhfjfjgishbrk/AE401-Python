#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:18:57 2020

@author: fdbfvuie
"""


scoreMath = input("請輸入數學成績 :")
scoreEnglish = input("請輸入英文成績 :")
try:
    scoreMath = int(scoreMath)
    scoreEnglish = int(scoreEnglish)
    if (scoreMath >= 90 and scoreEnglish >= 90):
        print("獎勵")
    elif (scoreMath < 60 and scoreEnglish < 60):
        print("處罰")
    elif (scoreMath < 60 or scoreEnglish < 60):
        print("再加油")
except ValueError:
    print("輸入錯誤")