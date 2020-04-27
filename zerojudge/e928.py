#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:18 2020

@author: fdbfvuie
"""

a1 = int(input())
n1 = [int(i) for i in input().split(" ")]

a2 = int(input())
n2 = [int(i) for i in input().split(" ")]

print(str(a1 + a2))

res = [0] * (a1 + a2 + 1)
for i in range(len(n1)):
    for j in range(len(n2)):
        res[i + j] += n1[i] * n2[j]

for i in range(len(res)):
    print(res[i], end=" ")