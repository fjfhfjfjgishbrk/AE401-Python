#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 11:48 2020

@author: fdbfvuie
"""

import sys
a = []
while 1:
    try:
        a.append(int(sys.stdin.readline().strip()))
        a.sort()
        if len(a) % 2 == 0:
            print((a[len(a) // 2] + a[len(a) // 2 - 1]) // 2)
        else:
            print(a[len(a) // 2])
    except:
        break