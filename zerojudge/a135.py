#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:11 2020

@author: fdbfvuie
"""

a = {"HELLO": "ENGLISH", "HOLA": "SPANISH", "HALLO": "GERMAN", "BONJOUR": "FRENCH", "CIAO": "ITALIAN", "ZDRAVSTVUJTE": "RUSSIAN"}
b = 1
while 1:
    c = input()
    if c == "#":
        break
    elif c in a:
        print("Case {}: {}".format(b, a[c]))
    else:
        print("Case {}: UNKNOWN".format(b))
    b += 1