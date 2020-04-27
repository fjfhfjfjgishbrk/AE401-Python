#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 20:40 2020

@author: fdbfvuie
"""

list = "豬鼠牛虎兔龍蛇馬羊猴雞狗"
while True:
    try:
        y = int(input())
        if y < 0:
            y += 1
        print(list[y % 12])
        
    except:
         break