#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:01:20 2020

@author: fdbfvuie
"""


import datetime
import time as t

time = datetime.datetime.now()

print(time.strftime("%Y") + "/" + time.strftime("%m")+ "/" + time.strftime("%d") + "  " + time.strftime("%a"))
print(time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S"))
print("Day " + time.strftime("%j") + "  Daylight savings time: " + str(bool(t.localtime().tm_isdst)))