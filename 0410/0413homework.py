#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:34:25 2020

@author: fdbfvuie
"""

"""
while True:
    try:
        textList = ["",0]
        txt = input()
        c = 0
        for i in range(len(txt) - 1):
            c += 1
            if txt[i] != txt[i + 1]:
                if c > textList[1]:
                    textList = [txt[i], c]
                c = 0
            elif i == len(txt) - 2:
                c += 1
                if c > textList[1]:
                    textList = [txt[i], c]
                c = 0
        print(textList[0], textList[1])
    except:
        break
"""

n = int(input())
for i in range(n):
    card = input.split(" ")
    cardnum = [int(i) % 13 for i in card]
    cardcolor = [(int(i) - 1) // 4 + 1 for i in card]