#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:17 2020

@author: fdbfvuie
"""

side1, side2, side3 = map(int, input().split())

side1 = int(side1)
side2 = int(side2)
side3 = int(side3)
bigSide = 0
if side1 > side2:
    bigSide = side1
else:
    bigSide = side2
if side3 > bigSide:
    bigSide = side3
squareSum = side1 ** 2 + side2 ** 2 + side3 ** 2
bigSide = bigSide ** 2
if squareSum > 2 * bigSide:
    print("acute triangle")
elif squareSum == 2 * bigSide:
    print("right triangle")
else:
    print("obtuse triangle")