#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:25 2020

@author: fdbfvuie
"""

n = int(input())
a = []
for i in range(n):
    s, p, l, w, r = map(str, input().split())
    a.append([s, int(p) * int(w) * int(r) / int(l)])
a.sort(key= lambda x: x[1], reverse=True)
for i in a:
    print(i[0])