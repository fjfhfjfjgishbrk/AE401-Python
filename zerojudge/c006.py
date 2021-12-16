#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:37 2020

@author: fdbfvuie
"""

while 1:
    a, b, c, d = map(int, input().split())
    if a + b + c + d == 0:
        break
    e = 80
    e += a - b if a > b else a + 40 - b
    e += 40
    e += c - b if c > b else c + 40 - b
    e += c - d if c > d else c + 40 - d
    print(e * 9)