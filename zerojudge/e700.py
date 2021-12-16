#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:16 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input().split("/")
        a = int(a[0]) * 100 + int(a[1])
        if a < 121:
            print("摩羯座")
        elif a < 220:
            print("水瓶座")
        elif a < 321:
            print("雙魚座")
        elif a < 421:
            print("牡羊座")
        elif a < 522:
            print("金牛座")
        elif a < 622:
            print("雙子座")
        elif a < 723:
            print("巨蟹座")
        elif a < 822:
            print("獅子座")
        elif a < 924:
            print("處女座")
        elif a < 1024:
            print("天秤座")
        elif a < 1123:
            print("天蠍座")
        elif a < 1223:
            print("射手座")
        else:
            print("摩羯座")
    except:
        break