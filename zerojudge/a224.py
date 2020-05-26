#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:20 2020

@author: fdbfvuie
"""

while True:
    try:
        a = input()
        b = []
        c = [0] * 26
        d = 0
        for i in a:
            if 64 < ord(i) < 91 or 96 < ord(i) < 123:
                c[ord(i.lower()) - 97] += 1
        for i in c:
            if i % 2 == 1:
                d += 1
        e = "yes !" if d <= 1 else "no..."
        print(e)
    except:
        break