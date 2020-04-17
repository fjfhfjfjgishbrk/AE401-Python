#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:14:12 2020

@author: fdbfvuie
"""


"""
def a(i):
    if i == 1:
        return 1
    else:
        return i * a(i - 1)
print(a(int(input("type a number: ")))) 
"""


"""
def a(i):
    if i == 1 or i == 2:
        return 1
    return a(i - 1) + a(i - 2)
n = int(input("type a number: "))
for num in range(n):
    print(a(num + 1))
"""


import pygame
import random as ran
import os

w = 1080
h = 640

def makesnow(n):
    retArray = []
    for i in range(n):
        retArray.append([ran.randint(0, w - 1), ran.randint(0, h), ran.randint(0, 255), ran.randint(0, 255), ran.randint(0, 255), ran.randint(3, 7)])
    return retArray

white = (255, 255, 255)
pygame.init()
size = (w, h)
snow = makesnow(70)
floorSnow = [0] * w
for i in range(w):
    floorSnow[i] = []
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("snow")


def drawcircle(x, y, r, g, b):
    pygame.draw.circle(screen, (r, g, b), (x, y), 4, 0)
def drawrect(x, y, r, g, b):
    pygame.draw.rect(screen, (r, g, b), [x - 2, y - 4, 4, 4], 0)
def drawpoly(x, y):
    pygame.draw.polygon(screen, (ran.randint(0, 255), ran.randint(0, 255), ran.randint(0, 255)), [pygame.Vector2(x, y), pygame.Vector2(x + 30, y), pygame.Vector2(x - 130, h), pygame.Vector2(x - 160, h)], 0)
    if x - 160 > w:
        return
    drawpoly(x + 30, y)
    

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    
    drawpoly(0, 0)
    for i in snow:
        drawcircle(i[0], i[1], i[2], i[3], i[4])
        i[1] += i[5]
        if i[1] > h:
            floorSnow[i[0]].append([i[2], i[3], i[4]])
            snow.remove(i)
            snow.append([ran.randint(0, w - 1), 0, ran.randint(0, 255), ran.randint(0, 255), ran.randint(0, 255), ran.randint(1, 10)])
    for i in range(len(floorSnow)):
        for j in range(len(floorSnow[i])):
            drawrect(i + 1, h - j * 4, floorSnow[i][j][0], floorSnow[i][j][1], floorSnow[i][j][2])
        if (ran.random() + 1) ** (len(floorSnow[i]) / 2) > 6:
            floorSnow[i].remove(floorSnow[i][0])
    
    
    clock.tick(20)
    pygame.display.flip()

    
pygame.display.quit()
pygame.quit()
os._exit(0)
    