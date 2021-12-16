#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 9 10:10 2020

@author: fdbfvuie
"""

aw = []
ab = []
n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    if c == 0:
        aw.append([a, b])
    else:
        ab.append([a, b])
bw = []
bb = []
n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    if c == 0:
        bw.append([a, b])
    else:
        bb.append([a, b])
c = 0
for i in bw:
    if i in aw:
        continue
    elif i in ab:
        c += 2
    else:
        c += 1
for i in bb:
    if i in ab:
        continue
    elif i in aw:
        c += 2
    else:
        c += 1
for i in aw:
    if i in bw or i in bb:
        continue
    else:
        c += 1
for i in ab:
    if i in bw or i in bb:
        continue
    else:
        c += 1
print(c)