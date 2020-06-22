#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:56 2020

@author: fdbfvuie
"""

a = "甲乙丙丁戊己庚辛壬癸"
b = "子丑寅卯辰巳午未申酉戌亥"
while 1:
    try:
        n = int(input())
        print(a[(n-1744) % 10] + b[(n-1744) % 12])
    except:
        break