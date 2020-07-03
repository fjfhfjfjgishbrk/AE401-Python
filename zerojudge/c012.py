#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 11:45 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input()
        b = {}
        for i in a:
            c = ord(i)
            if c in b:
                b[c] += 1
            else:
                b[c] = 1
        b = {k: v for k, v in sorted(b.items(), key=lambda item: (item[1], -item[0]))}
        for i, j in b.items():
            print(i, j)
        print()
    except:
        break