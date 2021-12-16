#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:40 2020

@author: fdbfvuie
"""

n = int(input())
print("INTERSECTING LINES OUTPUT")
for i in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    m1 = (y1 - y2) / (x1 - x2) if x1 != x2 else -1
    m2 = (y3 - y4) / (x3 - x4) if x3 != x4 else -1
    m3 = (y1 - y4) / (x1 - x4) if x1 != x4 else -1
    if m1==m2 and m1==m3:
        print("LINE")
    elif m1 == m2:
        print("NONE")
    else:
        if x1 == x2 and y3 == y4:
            x=x1
            y=y3
        elif x3 == x4 and y1 == y2:
            x=x3
            y=y1
        else:
            x=(-m1 * x1+y1+m2 * x3-y3) / (m2-m1)
            y=(-m1 * m2 * x1+m1 * m2 * x3+m2 * y1-m1 * y3) / (m2-m1)
        print("POINT {:.2f} {:.2f}".format(x, y))
print("END OF OUTPUT")