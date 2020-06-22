#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:06 2020

@author: fdbfvuie
"""

import math
while 1:
    try:
        a = round(float(input()) * 100)
        if a <= 10000:
            a = a * 0.9 + 800
        elif a <= 50000:
            a = a * 0.8
        else:
            a = a * 0.6
        a = math.floor(a)/100
        print("$" + "{:.2f}".format(a))
    except:
        break