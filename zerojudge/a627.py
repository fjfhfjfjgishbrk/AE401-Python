#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 10:53 2020

@author: fdbfvuie
"""

import math
while 1:
    try:
        c = [[250, 75], [400, 110], [500, 140], [750, 250]]
        p = 1000000000
        use = []
        a, b = map(int, input().split())
        for i in c:
            if b == 0:
                tempP = math.ceil(a/i[0]) * i[1]
                if tempP < p and math.ceil(a/i[0]) <= 8:
                    use = [math.ceil(a/i[0]), i[0], i[1], math.ceil(a/i[0])]
                    p = tempP
            elif b == 1:
                tempP = math.ceil(a/i[0]) * 2 * i[1]
                if tempP < p and math.ceil(a/i[0]) <= 4:
                    use = [math.ceil(a/i[0]) * 2, i[0], i[1], math.ceil(a/i[0])]
                    p = tempP
            elif b == 5:
                tempP = (math.ceil(a/i[0]) + 1) * i[1]
                if tempP < p and math.ceil(a/i[0]) <= 7:
                    use = [math.ceil(a/i[0]) + 1, i[0], i[1], math.ceil(a/i[0])]
                    p = tempP
        print("Qty: {} Disk: {}GB Price: ${}".format(str(use[0]), str(use[1]), str(use[2])))
        print("Total price of this {}GB array: ${}".format(str(use[3] * use[1]), str(use[0] * use[2])))
        print()
    except:
        break