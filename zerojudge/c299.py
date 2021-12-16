#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 11:31 2020

@author: fdbfvuie
"""

a = [int(i) for i in input().split()]
a.pop(0)
print(min(a), max(a), end=" ")
if max(a) - min(a) == len(a) - 1:
    print("yes")
else:
    print("no")