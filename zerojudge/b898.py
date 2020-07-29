#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:19 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = [int(j) for j in input().split()]
    print(max(a))