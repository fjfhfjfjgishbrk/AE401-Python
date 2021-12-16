#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:52 2020

@author: fdbfvuie
"""

while 1:
    try:
        n, m = map(int, input().split())
        a = 0
        b = 0
        c = 1
        e = []
        for i in range(n):
            d = int(input())
            e.append(d)
            b += d
            if c != m:
                c += 1
            else:
                a = max(a, b)
                b -= e[i - m + 1]
        for i in range(m - 1, 0, -1):
            b += e[m - i - 1]
            a = max(a, b)
            b -= e[-i]
        print(a)
    except:
        break