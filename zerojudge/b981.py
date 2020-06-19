#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 4 10:52 2020

@author: fdbfvuie
"""

d = {'hour': 3600000, "h": 3600000, "m": 60000, "s": 1000, "min": 60000, "ms": 1}
while True:
    try:
        a = input()
        b = 0
        c = []
        for i in range(len(a)-1):
            if a[i].isalpha() != a[i+1].isalpha():
                c.append(a[b:i+1])
                b = i+1
        c.append(a[b:])
        t = 0
        for i in range(0, len(c), 2):
            if c[i+1] == ".":
                c[i+2] = "{}.{}".format(c[i+1], c[i+2])
                continue
            t += int(float(c[i]) * int(d[c[i+1]]))
        print(t)
    except:
        break