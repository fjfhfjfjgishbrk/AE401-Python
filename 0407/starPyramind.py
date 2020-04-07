#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 10:46:01 2020

@author: fdbfvuie
"""

"""
for i in range(5):
    print(" "*(4-i)+"* "*(i+1))
for i in range(4):
    print(" "*(i+1)+"* "*(4-i))
"""

i = 0
while i < 5:
    print(" "*(4-i)+"* "*(i+1))
    i += 1
i = 0
while i < 4:
    print(" "*(i+1)+"* "*(4-i))
    i += 1