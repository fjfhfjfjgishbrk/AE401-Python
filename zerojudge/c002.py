#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:59 2020

@author: fdbfvuie
"""

while True:
    a = int(input())
    if a == 0:
        break
    b = 91 if a < 101 else a - 10
    print("f91({}) = {}".format(a, b))