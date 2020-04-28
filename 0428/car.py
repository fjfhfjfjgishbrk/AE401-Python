#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:26:51 2020

@author: fdbfvuie
"""


class car:
    def __init__(self, carNum, carType, size, speed):
        self.num = carNum
        self.carType = carType
        self.size = size
        self.speed = speed
        
    def distance(self, time):
        return self.speed * time
    
class fireTruck(car):
    def __init__(self, carNum, carType, size, speed, water, oil):
        super().__init__(carNum, carType, size, speed)
        self.water = water
        self.oilCost = oil
        
    def oilUsed(self, time):
        return self.distance(time) / self.oilCost