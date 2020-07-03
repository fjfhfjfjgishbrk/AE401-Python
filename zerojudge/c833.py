#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:10 2020

@author: fdbfvuie
"""

import sys
import re
n, m = map(int, input().split())
a = []
b = []
o = []
for i in range(n):
    s = sys.stdin.readline().strip()
    a.append(s)
    c = [j.start() for j in re.finditer("#", s)]
    b += c
c = ["X"] * m
b = list(dict.fromkeys(b))
for i in b:
    c[i] = "#"
for i in a:
    p = "".join(c) if "#" not in i else "#" * m
    print(p)