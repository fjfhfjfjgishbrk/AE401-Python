#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:19 2020

@author: fdbfvuie
"""

while 1:
    try:
        a, b = map(int, input().split())
        c = 0
        d = 1
        while c < a:
            if b == 0:
                c = a
                break
            c += d
            d += b
        if c == a:
            print("Go Kevin!!")
        else:
            print("No Stop!!")
    except:
        break