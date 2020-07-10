#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 10:39 2020

@author: fdbfvuie
"""

a = {}
while 1:
    try:
        s, e = map(int, input().split())
        print(s, e, end=" ")
        l = []
        for i in range(min(s, e), max(s, e) + 1, 1):
            b = [i]
            c = i
            d = 0
            while c > 1:
                if c % 2 == 1:
                    c = c * 3 + 1
                else:
                    c = int(c/2)
                if c in a:
                    d = a[c]
                    break
                else:
                    b.append(c)
            l.append(d + len(b))
            for j in range(len(b)):
                a[b[-j - 1]] = d + j + 1
        print(max(l))
    except:
        break