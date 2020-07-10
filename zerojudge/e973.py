#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 11:27 2020

@author: fdbfvuie
"""

n = input()
a = {}
for i in range(10):
    a[i] = n.count(str(i))
a = {k: v for k, v in sorted(a.items(), key=lambda item: (-item[1], item[0]))}
for i, j in a.items():
    if j == 0:
        continue
    else:
        print(i, end=" ")