#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:10 2020

@author: fdbfvuie
"""

n = int(input())
a = input().split()
a.insert(0, 0)
for i in range(1, n+1):
    a[i] = int(a[i-1]) + int(a[i])
n = int(input())
for i in range(n):
    s, e = map(int, input().split())
    print(a[e] - a[s-1])