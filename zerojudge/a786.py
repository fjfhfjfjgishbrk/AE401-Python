#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 1 11:55 2020

@author: fdbfvuie
"""

input()
a = {}
while True:
    b = input()
    if b != "[1337]":
        c, d = map(str, b.split(":"))
        a[c] = d
    else:
        break
while True:
    b = input()
    if b != "[3ND]":
        c = b.split()
        for i in c:
            if i in a:
                print(a[i], end=" ")
            else:
                print(i, end=" ")
        print()
    else:
        break