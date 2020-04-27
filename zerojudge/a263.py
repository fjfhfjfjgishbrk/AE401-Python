#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:41 2020

@author: fdbfvuie
"""

import datetime

while True:
    try:
        a = input()
        a = a.split(" ")
        b = input()
        b = b.split(" ")
        d1 = datetime.datetime(int(a[0]), int(a[1]), int(a[2]))
        d2 = datetime.datetime(int(b[0]), int(b[1]), int(b[2]))
        print(abs((d1-d2).days))

    except:
        break