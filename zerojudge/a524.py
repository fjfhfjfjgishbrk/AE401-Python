#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:12 2020

@author: fdbfvuie
"""

from itertools import permutations
while 1:
    try:
        n = int(input())
        a = []
        for i in range(n):
            a.append(i+1)
        b = permutations(a)
        c = []
        for i in list(b):
            c.append(int("".join(str(j) for j in i)))
        c.sort(reverse= True)
        for i in c:
            print(i)
    except:
        break