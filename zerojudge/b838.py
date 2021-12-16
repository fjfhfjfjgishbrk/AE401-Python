#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 9 09:57 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = 0
    b = input()
    c = 0
    if b[0] == ")":
        print("0")
        continue
    for j in b:
        if j == "(":
            a += 1
        elif j == ")":
            a -= 1
            c += 1
        if a < 0:
            break
    if a == 0:
        print(c)
    else:
        print("0")