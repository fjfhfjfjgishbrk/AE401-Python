#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 6 12:01 2020

@author: fdbfvuie
"""

import sys
from collections import Counter
n = int(input())
a = []
for i in range(n):
    a.append(sys.stdin.readline().strip())
b = dict(Counter(a))
b = {k: v for k, v in sorted(b.items(), key=lambda item: int(item[0]))}
for i in b:
    print(i, b[i])