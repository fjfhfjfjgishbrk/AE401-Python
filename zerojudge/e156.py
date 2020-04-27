#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:00 2020

@author: fdbfvuie
"""

import sys
sys.setrecursionlimit(1100)

def a(n):
    if n == 1:
        return 1
    else:
        return n + a(n - 1)

b = int(input())
print(a(b))