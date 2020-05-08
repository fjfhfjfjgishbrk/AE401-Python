#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 1 10:54 2020

@author: fdbfvuie
"""

txt = input()
for i in range(len(txt)):
    print(txt[i:] + txt[:i])