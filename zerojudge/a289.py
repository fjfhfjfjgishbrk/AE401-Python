#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:25 2020

@author: fdbfvuie
"""

import sys
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return 0
    else:
        return x % m

while True:
    try:
        a, b = map(int, sys.stdin.readline().strip().split())
        c = modinv(a, b)
        if c == 0:
            print("No Inverse")
        else:
            print(c)
    except:
        break