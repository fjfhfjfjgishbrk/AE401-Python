#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:53 2020

@author: fdbfvuie
"""

while 1:
    try:
        n = int(input())
        if n >= 40:
            print("100")
        elif n >= 20:
            print(str(80 + (n - 20) * 1))
        elif n >= 10:
            print(str(60 + (n - 10) * 2))
        else:
            print(n * 6)

    except:
        break