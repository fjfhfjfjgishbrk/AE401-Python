#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 20:26 2020

@author: fdbfvuie
"""

import sys

while True:
    text = sys.stdin.readline()
    text = text.strip()
    isSame = True

    if text == "":
        break

    for i in range(len(text) // 2):
        if text[i] == text[-i - 1]:
            continue
        else:
            isSame = False
            break

    if isSame:
        print("yes")
    else:
        print("no")