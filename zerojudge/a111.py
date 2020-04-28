#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:33 2020

@author: fdbfvuie
"""

while True:
    a = int(input())
    if a == 0:
        break
    print(int(a*(a+1)*(2*a+1)/6))