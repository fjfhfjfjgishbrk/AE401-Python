#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 12:21 2020

@author: fdbfvuie
"""

import math

num = input("")
abc = [int(i) for i in num.split(" ")]
ans = [0, 0]

if abc[1] ** 2 - 4 * abc[0] * abc[2] < 0:
    print("No real root")
else:
    d = int(math.sqrt(abc[1] ** 2 - 4 * abc[0] * abc[2]))
    ans[0] = (-abc[1] + d) / (2 * abc[0])
    ans[1] = (-abc[1] - d) / (2 * abc[0])
    ans.sort(reverse=True)

    if d == 0:
        print("Two same roots x=" + str(int(ans[0])))
    else:
        print("Two different roots x1=" + str(int(ans[0])) + " , x2=" + str(int(ans[1])))