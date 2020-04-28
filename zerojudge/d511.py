#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:59 2020

@author: fdbfvuie
"""

point = 0
for i in range(5):
    side1, side2, side3 = map(int, input().split(" "))
    if (side1 + side2 > side3 and side3 + side2 > side1 and side1 + side3 > side2):
        point += 1
print(point)