#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 10:08 2020

@author: fdbfvuie
"""

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
for i in range(n):
    b = input()
    c = ""
    for j in b:
        c += a[(a.find(j) + 3) % len(a)]
    print(c)