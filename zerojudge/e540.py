#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:16 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = input()
    b = 1
    c = 0
    for j in a:
        if j == "O":
            c += b
            b += 1
        else:
            b = 1
    print(c)