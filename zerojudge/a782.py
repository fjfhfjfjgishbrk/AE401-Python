#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 9 10:16 2020

@author: fdbfvuie
"""

while 1:
    a = input().split()
    if a[0] == "END":
        break
    b = "".join([i[0] for i in a]).upper()
    print(b, a[-1])