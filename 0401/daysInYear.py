#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:13:36 2020

@author: fdbfvuie
"""

dateList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dateListLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
season = ["winter", "spring", "summer", "autumn", "winter"]

year = input("Year: ")
month = input("Month: ")

try:
    year = int(year)
    month = int(month)
    leapyear = bool(year % 4 == 0)
    if (leapyear):
        print("days in year: 366  days in month: " + str(dateListLeap[month - 1]))
        print("season: " + str(season[month // 3]))
    else:
        print("days in year: 365  days in month: " + str(dateList[month - 1]))
        print("season: " + str(season[month // 3]))
    
except ValueError:
    print("input error")