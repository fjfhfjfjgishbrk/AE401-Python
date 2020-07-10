#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 9 09:48 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input()
        b = a.replace("-", "")
        c = 0
        d = "0123456789X"
        for i in range(len(b) - 1):
            c += int(b[i]) * (i + 1)
        if a[-1] == d[c % 11]:
            print("Right")
        else:
            print(a[:-1] + d[c % 11])
    except:
        break