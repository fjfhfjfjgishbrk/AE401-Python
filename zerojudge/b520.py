#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 10:18 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = [j.strip() for j in input().split(",")]
    b = [j.strip() for j in input().split(",")]
    c = len(set(a).intersection(b))
    print(c)