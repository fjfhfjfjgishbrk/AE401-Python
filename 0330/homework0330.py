#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:43:28 2020

@author: fdbfvuie
"""

import math

r = float(input("輸入圓半徑："))

print("\n圓半徑:", r)
print("周長:", round(r * 2 * math.pi, 3))
print("面積:", round(r**2 * math.pi, 3))