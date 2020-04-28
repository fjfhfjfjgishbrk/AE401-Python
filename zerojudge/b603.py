#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:52 2020

@author: fdbfvuie
"""

import math

while True:
    try:
        n = [int(i) for i in input().split(" ")]
        div = math.gcd(n[3] - n[1], (n[2] - n[0]) ** 2)
        a = (n[3] - n[1]) / div
        b = (n[2] - n[0]) ** 2 / div
        print(str(int(b)) + "y = " + str(int(a)) + "x^2 + " + str(int(-2 * a * n[0])) + "x + " + str(int(n[1] * b + a * n[0] ** 2)))

    except:
        break