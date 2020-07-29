#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:49 2020

@author: fdbfvuie
"""

import math
while 1:
    try:
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        c = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        s = (a + b + c) / 2
        d = (a * b * c) / (4 * math.sqrt(s * (s - a) * (s - b) * (s - c)))
        print("{:.2f}".format(d * 2 * math.pi))
    except:
        break