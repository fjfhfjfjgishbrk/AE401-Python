#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:45 2020

@author: fdbfvuie
"""

while 1:
    try:
        n = int(input())
        for i in range(2 ** n):
            txt = bin(i)[2:]
            x = txt.zfill(n)
            print(x)

    except:
        break