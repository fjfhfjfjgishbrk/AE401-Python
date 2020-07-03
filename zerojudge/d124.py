#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:45 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = "yes" if int(input()) % 3 == 0 else "no"
        print(a)
    except:
        break