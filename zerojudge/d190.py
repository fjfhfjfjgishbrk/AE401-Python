#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:47 2020

@author: fdbfvuie
"""

while 1:
    a = input()
    if a == "0":
        break
    b = [0] * 100
    c = input().split()
    for i in c:
        b[int(i) - 1] += 1
    for i in range(len(b)):
        print((str(i + 1) + " ") * b[i], end="")
    print()