#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 11:37 2020

@author: fdbfvuie
"""

import math
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)