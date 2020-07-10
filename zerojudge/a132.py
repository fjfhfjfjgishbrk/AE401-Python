#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 11:29 2020

@author: fdbfvuie
"""

while 1:
    n = int(input())
    if n == 0:
        break
    a = bin(n)[2:]
    b = a.count("1")
    print("The parity of {} is {} (mod 2).".format(a, str(b)))