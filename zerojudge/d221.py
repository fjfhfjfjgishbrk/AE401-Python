#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:51 2020

@author: fdbfvuie
"""

while 1:
    n = int(input())
    if n == 0:
        break
    a = [int(i) for i in input().split()]
    a.sort()
    d = 0
    while len(a) > 1:
        b = a[0] + a[1]
        c = 0
        d += b
        for i in range(len(a)):
            if a[i] > b:
                a.insert(i, b)
                a.pop(0)
                a.pop(0)
                c = 1
                break
        if c == 0:
            a.append(b)
            a.pop(0)
            a.pop(0)
    print(d)