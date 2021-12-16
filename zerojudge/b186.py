#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 10:42 2020

@author: fdbfvuie
"""

while 1:
    try:
        a, b, c = map(int, input().split())
        b += min(a//10, c//2)
        print("{} 個餅乾，{} 盒巧克力，{} 個蛋糕。".format(str(a), str(b), str(c)))
    except:
        break