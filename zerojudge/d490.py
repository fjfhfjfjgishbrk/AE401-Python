#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:04 2020

@author: fdbfvuie
"""

import math
a, b = map(int, input().split())
a = a + a % 2
b = b - b % 2
print(int((a + b) * ((b - a) / 2 + 1) / 2))