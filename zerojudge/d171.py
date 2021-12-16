#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:43 2020

@author: fdbfvuie
"""

import math
while 1:
    try:
        a, b = map(int, input().split())
        print(math.floor(b * math.log10(a) + 1))
    except:
        break