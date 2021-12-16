#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:05 2020

@author: fdbfvuie
"""

i = [2, 5, 5, 2, -1, -1]

def f(x):
    a = h(min(x % 6 + 6, x))
    b = g(x)
    if x > a:
        if x > 5:
            return f(x % 6 + 5) - 12 * (x // 6 - 1) - a
        else:
            return f(x - 1) - a
    if x < a:
        return f(b) - b
    else:
        return 1

def h(y):
    if y < 2:
        return -1
    else:
        return i[(y-2) % 6]

def g(z):
    if z <= 2:
        return z**2 - 1
    else:
        return 2
while 1:
    try:
        n = int(input())
        print(f(n))
    except:
        break