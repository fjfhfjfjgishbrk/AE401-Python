#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 9 09:43 2020

@author: fdbfvuie
"""

while 1:
    a, b, c = map(float, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        print("{:.2f} {:.2f}".format(a / b, b * c / a))