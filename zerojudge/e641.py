#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:35 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = ["BFPV", "CGJKQSXZ", "DT", "L", "MN", "R"]
        b = input()
        c = [0]
        e = 0
        for i in b:
            e = 0
            if c[-1] != 0:
                if i in a[c[-1] - 1]:
                    continue
            for j in range(len(a)):
                if i in a[j]:
                    if c[-1] == 0:
                        c.pop(-1)
                    c.append(j + 1)
                    e = 1
            if e == 0 and c[-1] != 0:
                c.append(0)
        if c[-1] == 0:
            c.pop(-1)
        print("".join([str(i) for i in c]))
    except:
        break