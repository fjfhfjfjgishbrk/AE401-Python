#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 09:21 2020

@author: fdbfvuie
"""

numInput = input()
date = numInput.split()
s = (int(date[0]) * 2 + int(date[1])) % 3
if s == 0:
    print("普通")
elif s == 1:
    print("吉")
else:
    print("大吉")