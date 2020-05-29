#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:33 2020

@author: fdbfvuie
"""

import re

n = int(input())
for i in range(n):
    text = input()
    print("Case {}:".format(str(i + 1)), end=" ")
    a = True
    b = ""
    c = 0
    for j in text:
        if a:
            a = False
            b = j
        else:
            if re.match("[0-9]", j):
                c = c * 10 + int(j)
            else:
                print(b*c, end="")
                b = j
                c = 0
    print(b*c)