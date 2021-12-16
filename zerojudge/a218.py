#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 10:10 2020

@author: fdbfvuie
"""


from collections import Counter
while 1:
    try:
        input()
        a = input().split()
        b = dict(Counter(a))
        b = {k: v for k, v in sorted(b.items(), key=lambda item: (-int(item[1]), int(item[0])))}
        print(" ".join(list(b)))
    except:
        break