#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 10:01:34 2020

@author: fdbfvuie
"""

import random
num = random.randint(1, 20)
count = 0
while count < 5:
    guess = input("guess a number: ")
    if num == int(guess):
        print("correct")
        break
    else:
        if num < int(guess):
            print("smaller")
        else:
            print("bigger")
    count += 1