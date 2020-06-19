#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:31 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input().split()
        s = 0
        maxdec = 0
        for i in a:
            b, c = map(str, i.split(":"))
            d = c.split(".")
            maxdec = max(maxdec, len(d[-1]) if len(d) == 2 else 0)
            if int(b) % 2 == 1:
                s += float(c)
            else:
                s -= float(c)
        print(round(s, maxdec) if str(s).split(".")[-1] != "0" else int(s))
    except:
        break