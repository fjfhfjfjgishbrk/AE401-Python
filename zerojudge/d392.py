#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:17 2020

@author: fdbfvuie
"""

while True:
    try:
        n = input().split()
        c = 0
        for i in n:
            c += int(i)
        print(c)

    except:
        break