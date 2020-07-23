#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:38 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = input().split()
    a[0] = int(a[0], 16)
    a[2] = int(a[2], 16)
    if a[1] == "+":
        print("{} + {} = {}".format(bin(a[0])[2:].zfill(13), bin(a[2])[2:].zfill(13), a[0] + a[2]))
    else:
        print("{} - {} = {}".format(bin(a[0])[2:].zfill(13), bin(a[2])[2:].zfill(13), a[0] - a[2]))