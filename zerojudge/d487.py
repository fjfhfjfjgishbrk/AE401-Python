#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:09 2020

@author: fdbfvuie
"""

while 1:
    try:
        n = int(input())
        if n == 0:
            print("0! = 1 = 1")
        else:
            print(str(n) + "! = ", end="")
            a = []
            for i in range(n, 0, -1):
                a.append(str(i))
            print(" * ".join(a), end=" = ")
            b = 1
            for i in range(n):
                b *= i + 1
            print(b)
    except:
        break