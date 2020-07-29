#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:20 2020

@author: fdbfvuie
"""

b = 1
while 1:
    a = int(input())
    if a < 0:
        break
    else:
        c = 0
        while a > 2 ** c:
            c += 1
        print("Case {}: {}".format(b, c))
        b += 1