#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 9 10:44 2020

@author: fdbfvuie
"""

while 1:
    try:
        r, c, m = map(int, input().split())
        a = []
        for i in range(r):
            a.append(input().split())
        n = input().split()
        n.reverse()
        for i in n:
            atemp = []
            if i == "0":
                for j in range(len(a[0]) - 1, -1, -1):
                    b = [i[j] for i in a]
                    atemp.append(b)
            else:
                atemp = a.copy()
                atemp.reverse()
            a = atemp.copy()
        print(len(a), len(a[0]))
        for i in a:
            print(" ".join(i))
    except:
        break