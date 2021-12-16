#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 7 21:18 2020

@author: fdbfvuie
"""

while True:
    try:
        num = [int(i) for i in input().split(" ")]
        add = [num[0] - num[1], num[1]]
        if num[0] == num[1]:
            add = [3, num[0] - 3]
        add.sort()
        print(str(add[0]) + "+" + str(add[1]) + "=" + str(num[0]))
    except:
        break