#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:32 2020

@author: fdbfvuie
"""

n = int(input())
num = [int(i) for i in input().split()]
num.sort()
print(" ".join([str(i) for i in num]))