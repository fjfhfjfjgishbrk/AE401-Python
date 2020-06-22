#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:25 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = [int(i) for i in input().split()]
    a.pop(0)
    print("{:.2f}".format(round(sum(a)/len(a), 2)))