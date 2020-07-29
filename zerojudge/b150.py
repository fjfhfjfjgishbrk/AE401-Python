#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:24 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = []
        for i in range(12):
            a.append(int(input()))
        m = 0
        s = 0
        c = 0
        for i in range(len(a)):
            m += 300
            b = max((m - a[i]) // 100, 0)
            m -= b * 100 + a[i]
            s += b * 100
            if m < 0:
                c = i + 1
                break
        if c != 0:
            print("-{}".format(c))
        else:
            print(int(m + s * 1.2))
        print()
        input()
    except:
        break