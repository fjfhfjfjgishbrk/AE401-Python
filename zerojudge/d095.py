#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 10:53 2020

@author: fdbfvuie
"""

while 1:
    h, m = map(int, input().split(":"))
    if h == 0 and m == 0:
        break
    md = 6 * m
    hd = 30 * h + 0.5 * m
    d = max(md - hd, hd - md)
    d = 360 - d if d > 180 else d
    print("{:.3f}".format(d))