#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 9 11:57 2020

@author: fdbfvuie
"""

import math
while True:
    try:
        A, B = input().split()
        print(math.gcd(int(A), int(B)))

    except:
        break