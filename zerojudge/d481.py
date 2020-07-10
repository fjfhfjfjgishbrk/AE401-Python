#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 9 11:24 2020

@author: fdbfvuie
"""

import sys
while 1:
    try:
        a, b, c, d = map(int, input().split())
        if b != c:
            print("Error")
            continue
        aa = []
        bb = []
        for i in range(a):
            aa.append([int(i) for i in sys.stdin.readline().strip().split()])
        for i in range(c):
            bb.append([int(i) for i in sys.stdin.readline().strip().split()])
        result = []
        for i in range(len(aa)):
            temp = []
            for j in range(len(bb[0])):
                n = 0
                for k in range(len(bb)):
                    n += bb[k][j] * aa[i][k]
                temp.append(n)
            result.append(temp.copy())
        for i in result:
            print(" ".join([str(j) for j in i]))
    except:
        break