#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:19 2020

@author: fdbfvuie
"""

while 1:
    try:
        d, e = map(int, input().split())
        print(int(d*(d+1)*e*(e+1)/4))
    except:
        break