#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:12 2020

@author: fdbfvuie
"""

while 1:
    try:
        r, c, m = map(int, input().split())
        a = []
        for i in range(r):
            a.append([int(j) for j in input().split()])
        step = [int(i) for i in input().split()]
        for i in range(len(step)):
            tempA = []
            if step[-i-1] == 0:
                for j in range(len(a[0])):
                    tempA.append([k[-j-1] for k in a])
            else:
                for j in range(len(a)):
                    tempA.append(a[-j-1])
            a = tempA
        print(len(a), len(a[0]))
        for i in a:
            print(" ".join([str(j) for j in i]))
    except:
        break