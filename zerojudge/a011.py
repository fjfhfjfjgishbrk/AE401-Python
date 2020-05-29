#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:38 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input()
        b = 0
        for i in range(1, len(a)):
            if a[i].isalpha() == False and a[i - 1].isalpha() == True:
                b += 1
        if a[-1].isalpha() == True:
                b += 1
        print(b)
    except:
        break