#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:28 2020

@author: fdbfvuie
"""

while 1:
    try:
        a, b, c = map(int, input().split())
        d = max(a+10*b+c, 10*a+b+c, a*(10*b+c), (10*a+b)*c, a+b+c, a+b*c, a*b+c, a*b*c)
        print(d)
    except:
        break