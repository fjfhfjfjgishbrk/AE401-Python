#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:56 2020

@author: fdbfvuie
"""

while True:
    try:
        n = int(input())
        a = input().split(" ")
        print(max([int(i) for i in a]))

    except:
        break