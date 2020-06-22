#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 4 11:10 2020

@author: fdbfvuie
"""

import math
d = {'gb': 8000000000,  "mb": 8000000, "kb": 8000, "byte": 8, "bit": 1, "g": 8000000000, "m": 8000000, "k": 8000}
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
            c[i] = math.modf(float(c[i]))[0] * 1.25 + math.modf(float(c[i]))[1] if c[i+1] != "kb" else float(c[i])
            t += int(c[i] * int(d[c[i+1]]))
        print(t)
    except:
        break