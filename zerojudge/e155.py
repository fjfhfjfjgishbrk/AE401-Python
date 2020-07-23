#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:39 2020

@author: fdbfvuie
"""

while 1:
    n = int(input())
    if n == 0:
        break
    a = []
    b = []
    for i in range(n):
        a.append(i + 1)
    while len(a) >= 2:
        b.append(str(a[0]))
        a.pop(0)
        a.append(a[0])
        a.pop(0)
    print("Discarded cards: {}".format(", ".join(b)))
    print("Remaining card: {}".format(a[0]))