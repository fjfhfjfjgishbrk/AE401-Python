#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 9 10:53 2020

@author: fdbfvuie
"""

import random
for i in range(100):
    a = random.randint(1, 10**6 - 1)
    b = random.randint(1, 10**6 - 1)
    print(a, b, a+b)