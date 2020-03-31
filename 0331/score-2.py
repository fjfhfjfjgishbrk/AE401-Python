#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:13:26 2020

@author: fdbfvuie
"""


score = input("請輸入成績 :")
try:
    score = int(score)
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("E")
except ValueError:
    print("輸入錯誤")