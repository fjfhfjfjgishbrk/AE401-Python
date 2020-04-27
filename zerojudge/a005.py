#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:12 2020

@author: fdbfvuie
"""

n = int(input())

for i in range(n):
    num = [int(i) for i in input().split(" ")]
    for j in num:
        print(j, end=" ")

    if num[0] + num[2] == 2 * num[1]:
        print(num[-1] + num[1] - num[0])
    else:
        print(int(num[-1] * (num[1] / num[0])))