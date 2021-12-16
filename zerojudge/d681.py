#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 11:21 2020

@author: fdbfvuie
"""

while 1:
    try:
        inp = input()
        a = inp.split()
        outstr = inp.replace(" and ", "&&").replace(" or ", "||").strip()
        for i in range(0, len(a), 2):
            a[i] = int(a[i], 2)
        for i in range(2, len(a), 2):
            if a[i-1] == "or":
                a[i] = a[i-2] | a[i]
            else:
                a[i] = a[i-2] & a[i]
        print("{} = {}".format(outstr, bin(a[-1])[2:].zfill(5)))
    except:
        break