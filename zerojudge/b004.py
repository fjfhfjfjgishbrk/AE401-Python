#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:45 2020

@author: fdbfvuie
"""

import math
while 1:
    try:
        a, b = map(int, input().split())
        print("{:.3f}".format(round(math.pi * (b/2) * math.sqrt((b/2) ** 2 - (a/2) ** 2), 3)))
    except:
        break