#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:40 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    g, l = map(int, input().split())
    if l % g != 0:
        print("-1")
    else:
        print(g, l)