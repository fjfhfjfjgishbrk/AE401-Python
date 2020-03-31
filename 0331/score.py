#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:58:09 2020

@author: fdbfvuie
"""


score = input("請輸入成績 :")
try:
    score = int(score)
    if score >= 60:
        print("及格")
    else:
        print("不及格")
except ValueError:
    print("輸入錯誤")
