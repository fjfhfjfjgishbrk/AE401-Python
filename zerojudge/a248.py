#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:53 2020

@author: fdbfvuie
"""

import sys
import decimal

inp = sys.stdin.readlines()
for i in inp:
    a, b, n = map(int, i.strip().split(" "))
    decimal.getcontext().prec = len(str(a // b)) + n if a // b != 0 else n
    decimal.getcontext().rounding = "ROUND_DOWN"
    print(format(decimal.Decimal(a)/decimal.Decimal(b),"."+str(int(n))+"f"))