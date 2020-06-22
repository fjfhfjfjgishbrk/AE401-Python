#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 4 11:15 2020

@author: fdbfvuie
"""

while True:
    a = input().lower().strip()
    b = 0
    c = False
    if a == "0":
        break
    for i in a:
        if i.isalpha():
            b += ord(i) - 96
        else:
            c = True
            break
    if c:
        print("Fail")
    else:
        print(b)