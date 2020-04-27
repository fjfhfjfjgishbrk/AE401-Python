#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:45 2020

@author: fdbfvuie
"""

import math
while True:
    try:
        n = [int(i) for i in input().split(" ")]
        print(math.floor(n[1] * math.log10(n[0])) + 1)

    except:
        break