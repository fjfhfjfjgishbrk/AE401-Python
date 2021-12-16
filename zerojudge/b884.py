#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 1 10:51 2020

@author: fdbfvuie
"""

import math
n = int(input())
for i in range(n):
    a = input().split(" ")
    yee = 100 - math.sqrt(abs(int(a[0])) + abs(int(a[1]))) ** 2
    if yee <= 0:
        print("evil!!")
    elif yee <= 30:
        print("sad!")
    elif yee <= 60:
        print("hmm~~")
    elif yee < 100:
        print("Happyyummy")
    else:
        print("evil!!")
