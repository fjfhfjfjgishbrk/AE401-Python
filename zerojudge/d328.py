#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:33 2020

@author: fdbfvuie
"""

while 1:
    try:
        s1, s2, s3 = map(int, input().split())
        s = s1+s2+s3+((s2*s3)/(2*s1))+((s3*s1)/(2*s2))+((s1*s2)/(2*s3))
        print("{:.2f}".format(s))
    except:
        break