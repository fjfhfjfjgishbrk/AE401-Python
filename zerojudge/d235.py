#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:04 2020

@author: fdbfvuie
"""

while 1:
    a = int(input())
    if a == 0:
        break
    elif a % 11 == 0:
        print("{} is a multiple of 11.".format(str(a)))
    else:
        print("{} is not a multiple of 11.".format(str(a)))