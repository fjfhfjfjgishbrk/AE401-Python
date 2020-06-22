#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:34 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = input()
    b = []
    c = "Yes"
    for j in a:
        if j == "(" or j == "[":
            b.append(j)
        else:
            if not b:
                c = "No"
                break
            if b[-1] == "(" and j == ")" or b[-1] == "[" and j == "]":
                b.pop()
            else:
                c = "No"
                break
    if b:
        c = "No"
    print(c)