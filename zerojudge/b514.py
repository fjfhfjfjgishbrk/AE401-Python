#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:06 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a, b, e, c, d, f = map(int, input().split())
    p = a*d - b*c
    q = e*d - b*f
    r = a*f - e*c
    print(int(q/p), int(r/p))