#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:11 2020

@author: fdbfvuie
"""

n = int(input())
a = input().split(" ")
c = [0, 0, 0]

for i in a:
    if i == "":
        continue
    c[int(i) - 1] += 1

for i in range(3):
    for j in range(c[i]):
        print(i + 1, end=" ")