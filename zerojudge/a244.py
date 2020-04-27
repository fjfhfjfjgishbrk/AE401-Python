#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:41 2020

@author: fdbfvuie
"""

n = int(input())

for i in range(n):
    a = [int(j) for j in input().split(" ")]
    if a[0] == 1:
        print(a[1] + a[2])
    if a[0] == 2:
        print(a[1] - a[2])
    if a[0] == 3:
        print(a[1] * a[2])
    if a[0] == 4:
        print(a[1] // a[2])