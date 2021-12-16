#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:18 2020

@author: fdbfvuie
"""

import math
while 1:
    try:
        txt = input()
        print(txt)
        txt = txt.lower()
        a = []
        b = True
        for i in txt:
            if i.isalnum():
                a.append(i)
        for i in range(math.floor(len(a)/2)):
            if a[i] != a[-i-1]:
                b = False
        if b:
            print("-- is a palindrome")
        else:
            print("-- is not a palindrome")
    except:
        break