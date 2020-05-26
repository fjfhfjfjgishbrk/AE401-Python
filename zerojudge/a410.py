#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:09 2020

@author: fdbfvuie
"""

a, b, c, d, e, f = map(int, input().split())
if (a*e - b*d) == 0:
    if (c*e - b*f) == 0 and (a*f - c*d) == 0:
        print("Too many")
    else:
        print("No answer")
else:
    x = (c*e - b*f) / (a*e - b*d)
    y = (a*f - c*d) / (a*e - b*d)
    print("x={:.2f}".format(x))
    print("y={:.2f}".format(y))