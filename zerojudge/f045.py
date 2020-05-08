#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 7 21:10 2020

@author: fdbfvuie
"""

while True:
    try:
        inp = input()
        n = [int(i) for i in inp]
        n.sort()
        endNum = int(inp[-3:])
        if n[-1] ** 2 + n[-2] ** 2 == endNum:
            print("Good Morning!")
        elif n[-1] ** 2 + n[-2] ** 2 == 0 and endNum == 1:
            print("Good Morning!")
        else:
            print("SPY!")
    except:
        break