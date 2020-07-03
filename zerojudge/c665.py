#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:14 2020

@author: fdbfvuie
"""

def baseN(num, b):
    return "" if num == 0 else baseN(num // b, b) + "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[num % b]

while 1:
    try:
        a, b, c = map(str, input().split())
        d = int(a, int(b))
        print(baseN(d, int(c)))
    except:
        break