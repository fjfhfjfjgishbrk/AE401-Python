#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:51 2020

@author: fdbfvuie
"""

import sys
n = sys.stdin.readlines()
try:
    a = int(n[0].strip())
except:
    n = n[0].strip().split("\r")

for i in range(int(n[0].strip())):
    g, a, h, w = map(int, n[i + 1].strip().split())
    if g == 1:
        print("{:.2f}".format(13.7*w+5*h-6.8*a+66))
    else:
        print("{:.2f}".format(9.6*w+1.8*h-4.7*a+655))