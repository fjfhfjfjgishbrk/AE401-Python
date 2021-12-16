#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:10 2020

@author: fdbfvuie
"""

n = int(input())
b = ["one", "two", "three"]
for i in range(n):
    a = input()
    c = 0
    d = 0
    if len(a) == 3:
        for j in range(3):
            if a[j] == b[0][j]:
                c += 1
            if a[j] == b[1][j]:
                d += 1
        if c >= 2:
            print("1")
        elif d >= 2:
            print("2")
    elif len(a) == 5:
        for j in range(5):
            if a[j] == b[2][j]:
                c += 1
        if c >= 4:
            print("3")