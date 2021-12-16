#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:59 2020

@author: fdbfvuie
"""

import math
n = int(input())
for i in range(n):
    d = int(input())
    print(math.floor((-1 + math.sqrt(1 + 8 * d)) / 2))