#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:27 2020

@author: fdbfvuie
"""

b = 1
while 1:
    p, e, i, d = map(int, input().split())
    if p == -1:
        break
    a = p * 5544 + e * 14421 + i * 1288 - d
    a += 21252 if a < 0 else 0
    a = a % 21252
    a = 21252 if a == 0 else a
    print("Case {}: the next triple peak occurs in {} days.".format(str(b), str(a)))
    b += 1