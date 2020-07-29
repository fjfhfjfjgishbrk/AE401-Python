#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:29 2020

@author: fdbfvuie
"""

while 1:
    try:
        a, b, c, d, f = map(float, input().split())
        e = ((d-f)*(b-c))/(a-c)+f
        print("{0:.6f}".format(e))
    except:
        break