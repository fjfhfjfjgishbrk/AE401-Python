#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 11:58 2020

@author: fdbfvuie
"""

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
if c >= b and e >= b and e >= d:
    print("Happy")
else:
    print("QQ")