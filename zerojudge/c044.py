#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:51 2020

@author: fdbfvuie
"""

n = int(input())
b = {}
for i in range(n):
    a = input()
    for j in a:
        if j.isalpha():
            if j.upper() in b:
                b[j.upper()] += 1
            else:
                b[j.upper()] = 1
b = {k: v for k, v in sorted(b.items(), key=lambda item: (-item[1], item[0]))}
for i, j in b.items():
    print(i, j)