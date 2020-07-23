#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:09 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    b = {}
    a = input()
    for j in a:
        if j.isalpha():
            if j.lower() in b:
                b[j.lower()] += 1
            else:
                b[j.lower()] = 1
    b = {k: v for k, v in sorted(b.items(), key=lambda item: (-item[1], item[0]))}
    for i in b.keys():
        if b[i] != max(b.values()):
            break
        print(i, end="")
    print()