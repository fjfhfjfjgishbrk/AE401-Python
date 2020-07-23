#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:21 2020

@author: fdbfvuie
"""

import math
while 1:
    try:
        s, d = map(int, input().split())
        d += s * (s - 1) // 2
        print(math.ceil((-1 + math.sqrt(1 + 8 * d)) / 2))
    except:
        break