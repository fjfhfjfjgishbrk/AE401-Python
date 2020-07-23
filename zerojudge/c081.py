#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:49 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = []
        b = [int(i) for i in input().split()]
        c = ["", -1]
        d = ["BCG", "BGC", "CBG", "CGB", "GBC", "GCB"]
        for i in range(0, 9, 3):
            a.append([b[i], b[i+1], b[i+2]])
        for i in d:
            e = 0
            for j in range(len(i)):
                if i[j] == "B":
                    e += a[j][1] + a[j][2]
                elif i[j] == "C":
                    e += a[j][0] + a[j][1]
                else:
                    e += a[j][0] + a[j][2]
            if e < c[1] or c[1] == -1:
                c = [i, e]
        print(c[0], c[1])
    except:
        break