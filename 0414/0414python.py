#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:36:19 2020

@author: fdbfvuie
"""

"""
s = 0
for i in range(101):
    s += i
print(s)
"""

"""
s = 0
i = 0
while i <= 100:
    s += i
    i += 1
print(s)
"""


def a(i):
    if i == 100:
        return i
    else:
        return i + a(i + 1)
print(a(0)) 


