#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:01 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = {}
        b = input()
        for i in b:
            if i.isalpha():
                if i in a:
                    a[i] += 1
                else:
                    a[i] = 1
        a = {i: j for i, j in sorted(a.items(), key=lambda item: (-item[1], item[0]))}
        c = 0
        for i, j in a.items():
            if c > j:
                print(" " + str(c))
                break
            print(i, end="")
            c = max(c, j)
    except:
        break