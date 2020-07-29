#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:50 2020

@author: fdbfvuie
"""

a = int(input())
for i in range(a):
    b = int(input())
    c = 10000000000000
    d = 0
    for j in range(b):
        m, s = map(int, input().split())
        c = min(c, m*60+s)
        d += m*60+s
    d = d // b
    print("Track {}:".format(i+1))
    print("Best Lap: {} minute(s) {} second(s).".format(c//60, c%60))
    print("Average: {} minute(s) {} second(s).".format(d//60, d%60))
    print()