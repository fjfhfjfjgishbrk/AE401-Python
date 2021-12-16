#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:43 2020

@author: fdbfvuie
"""

while 1:
    try:
        n = int(input())
        score = [int(i) for i in input().split()]
        score.sort()
        print(" ".join([str(i) for i in score]))
        for i in range(len(score)):
            if score[i] >= 60:
                if i == 0:
                    print("best case")
                    print(score[0])
                    break
                else:
                    print(score[i - 1])
                    print(score[i])
                    break
            if i == len(score) - 1:
                print(score[-1])
                print("worst case")
    except:
        break