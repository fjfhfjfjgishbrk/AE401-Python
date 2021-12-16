#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:59 2020

@author: fdbfvuie
"""

a, b = map(int, input().split())
a += 2
b += 30
if b >= 60:
    b -= 60
    a += 1
a = a % 24
print("{}:{}".format('{:02d}'.format(a), '{:02d}'.format(b)))