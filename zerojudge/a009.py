#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 20:08 2020

@author: fdbfvuie
"""

import sys

while 1:
    text = sys.stdin.readline()
    if text == "":
        break

    for i in text:
        print(chr(ord(i)-7),end="")

    print("", end="\n")