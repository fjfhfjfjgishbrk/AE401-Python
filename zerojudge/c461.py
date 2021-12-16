#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:47 2020

@author: fdbfvuie
"""

a, b, c = map(int, input().split())
d = 1
a = 1 if a > 1 else a
b = 1 if b > 1 else b
if (a and b) == c:
    print("AND")
    d = 0
if (a or b) == c:
    print("OR")
    d = 0
if (a != b) == c:
    print("XOR")
    d = 0
if d:
    print("IMPOSSIBLE")