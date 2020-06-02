#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:06 2020

@author: fdbfvuie
"""

a, b, c = map(int, input().split())
s = (a+b+c)/2
area = s * (s - a) * (s - b) * (s - c)
print(int(area))