#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:14 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input().split()
        b = 0
        for i in a:
            if i.isnumeric():
                b += int(i)
        print(b)
    except:
        break