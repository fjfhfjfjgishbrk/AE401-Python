#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:20 2020

@author: fdbfvuie
"""

c = 1
while 1:
    try:
        n = int(input())
        a = [int(i) for i in input().split()]
        b = []
        e = 0
        for i in range(n):
            for j in range(i, n):
                d = a[i] + a[j]
                if d in b:
                    e = 1
                    break
                else:
                    b.append(d)
        if e == 0:
            print("Case #{}: It is a B2-Sequence.".format(c))
        else:
            print("Case #{}: It is not a B2-Sequence.".format(c))
        print()
        c += 1
    except:
        break