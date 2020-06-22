#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 4 11:52 2020

@author: fdbfvuie
"""

n = int(input())
a = {}
for i in range(n):
    b, c = map(str, input().split())
    a[b] = float(c)
d = {i: j for i, j in sorted(a.items(), key=lambda item: item[1])}
e = []
for i in range(int(n/8)):
    e.append([])
f = [i for i, j in d.items()]
g = 0
countUp = True
for i in range(n):
    e[g].append(f[i])
    g = g + 1 if countUp else g - 1
    if g == int(n/8):
        g -= 1
        countUp = False
    elif g == -1:
        g += 1
        countUp = True
h = []
for i in e:
    h.append([])
    for j in "75312468":
        h[-1].append(i[int(j) - 1])
for i in range(len(h)):
    print("{} {}".format(str(i+1), " ".join(h[i])))