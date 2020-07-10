#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 6 10:17 2020

@author: fdbfvuie
"""

from collections import Counter
input()
a = input().split()
b = dict(Counter(a))
b = {k: v for k, v in sorted(b.items(), key=lambda item: (-int(item[1]), int(item[0])))}
c = True
for i in b:
    if c:
        d = b[i]
        c = False
    if b[i] == d:
        print(i, b[i])
    else:
        break