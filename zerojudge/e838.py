#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:21 2020

@author: fdbfvuie
"""

n = int(input())
bomb = [[],[]]
for i in range(n):
    a = input()
    for j in range(len(a)):
        if a[j] == "*":
            bomb[0].append(j)
            bomb[1].append(i)
for i in range(n):
    for j in range(n):
        if j in bomb[0] or i in bomb[1]:
            print("*", end="")
        else:
            print("0", end="")
    print()