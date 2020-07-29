#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:33 2020

@author: fdbfvuie
"""

while 1:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 0:
        break
    if x1 == x2 and y1 == y2:
        print("0")
    elif x1 == x2 or y1 == y2:
        print("1")
    elif abs((x1 - x2) / (y1 - y2)) == 1:
        print("1")
    else:
        print("2")