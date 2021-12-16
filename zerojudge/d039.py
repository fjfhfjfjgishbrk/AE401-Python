#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:34 2020

@author: fdbfvuie
"""

import math
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(math.ceil((a - 2) / 3) * math.ceil((b - 2) / 3))