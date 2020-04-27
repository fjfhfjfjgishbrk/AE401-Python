#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:30 2020

@author: fdbfvuie
"""

n = int(input())
num = [int(i) for i in input().split(" ")]
dict = {}

for i in range(n):
    dict[num[2 * i]] = num[2 * i + 1]

n = int(input())
num = [int(i) for i in input().split(" ")]

for i in range(n):
    if num[2 * i] in dict:
        dict[num[2 * i]] += num[2 * i + 1]
    else:
        dict[num[2 * i]] = num[2 * i + 1]

isNull = True
for key in sorted(dict, reverse=True):
    if dict[key] == 0:
        continue
    else:
        isNull = False
        print(str(key) + ":" + str(dict[key]))

if isNull:
    print("NULL!")