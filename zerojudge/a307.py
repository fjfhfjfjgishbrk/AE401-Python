#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:23 2020

@author: fdbfvuie
"""

a = int(input())
if a < 0:
    print("-{}".format(int(str(a)[:0:-1])))
else:
    print(int(str(a)[::-1]))