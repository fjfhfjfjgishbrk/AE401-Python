#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:28 2020

@author: fdbfvuie
"""

n = int(input())
a = []
for i in range(n):
    b = input()
    if b[0] == "1":
        a.pop()
    elif b[0] == "2":
        print(a[-1])
    else:
        b = b.split()
        a.append(b[-1])