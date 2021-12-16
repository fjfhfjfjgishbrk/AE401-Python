#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:20 2020

@author: fdbfvuie
"""

import datetime

a = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
c = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
while 1:
    m, d, y = map(int, input().split())
    if m + d + y == 0:
        break
    if y > 1752 or (y == 1752 and m >= 9 and d >= 14):
        try:
            b = datetime.datetime(y, m, d)
            print("{} {}, {} is a {}".format(b.strftime("%B"), d, y, b.strftime("%A")))
        except:
            print("{}/{}/{} is an invalid date.".format(m, d, y))
            continue
    elif y == 1752 and m == 9 and d >= 3:
        print("{}/{}/{} is an invalid date.".format(m, d, y))
    else:
        if y % 400 == 0:
            try:
                b = datetime.datetime(y, m, d) + datetime.timedelta(days=5 + y // 100 - y // 400)
                print("{} {}, {} is a {}".format(c[m - 1], d, y, b.strftime("%A")))
            except:
                print("{}/{}/{} is an invalid date.".format(m, d, y))
        elif y % 100 == 0:
            if m > 2:
                try:
                    b = datetime.datetime(y, m, d) + datetime.timedelta(days=5 + y // 100 - y // 400)
                    print("{} {}, {} is a {}".format(c[m - 1], d, y, b.strftime("%A")))
                except:
                    print("{}/{}/{} is an invalid date.".format(m, d, y))
            elif m == 2 and d == 29:
                b = datetime.datetime(y, m, 28) + datetime.timedelta(days=5 + y // 100 - y // 400)
                print("{} {}, {} is a {}".format(c[m - 1], d, y, b.strftime("%A")))
            else:
                try:
                    b = datetime.datetime(y, m, d) + datetime.timedelta(days=4 + y // 100 - y // 400)
                    print("{} {}, {} is a {}".format(c[m - 1], d, y, b.strftime("%A")))
                except:
                    print("{}/{}/{} is an invalid date.".format(m, d, y))
        else:
            try:
                b = datetime.datetime(y, m, d) + datetime.timedelta(days=5 + y // 100 - y // 400)
                print("{} {}, {} is a {}".format(c[m - 1], d, y, b.strftime("%A")))
            except:
                print("{}/{}/{} is an invalid date.".format(m, d, y))