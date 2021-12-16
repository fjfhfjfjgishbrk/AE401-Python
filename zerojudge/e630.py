#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 8 10:35 2020

@author: fdbfvuie
"""

a = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
b = {"十": 10, "百": 100, "千": 1000}
c = {"萬": 10000, "億": 100000000, "兆": 1000000000000}

while 1:
    try:
        tempSum1 = 0
        tempSum2 = 0
        finalSum = 0
        text = input()
        for i in text:
            if i in a:
                tempSum1 += a[i]
            if i in b:
                tempSum2 += tempSum1 * b[i]
                tempSum1 = 0
            if i in c:
                finalSum += (tempSum1 + tempSum2) * c[i]
                tempSum1 = 0
                tempSum2 = 0
        finalSum += tempSum1 + tempSum2
        print(finalSum)
    except:
        break