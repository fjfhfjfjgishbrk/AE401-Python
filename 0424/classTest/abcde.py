#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:14:02 2020

@author: fdbfvuie
"""

import math

class people():
    def __init__(self, name, w, h):
        self.name = name
        self.weight = w
        self.height = h
        
    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)
    
class apple(people):
    def __init__(self, name, w, h, r):
        super().__init__(name, w, h)
        self.radius = r
        
    def volume(self):
        return 4 / 3 * math.pi * (self.radius ** 2)
    
class circle(apple):
    circleR = 10
    
    def __init__(self, name, w, h, r):
        super().__init__(name, w, h, r)
        
    def area(self):
        return self.circleR * math.pi ** 2
        
    