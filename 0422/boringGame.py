#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:04:36 2020

@author: fdbfvuie
"""

import pygame
import random as ran
import os

def makeThings(count):
    a = []
    for i in range(count):
        a.append([ran.randint(0, w - 40), ran.randint(0, h - 40), ran.randint(0, 255), ran.randint(0, 255), ran.randint(0, 255), 40, 40, 40, 0])
    return a

def drawRect(x, y, r, g, b, rw, rl):
    pygame.draw.rect(screen, (r, g, b), [x, y, rw, rl], 0)
    
def collision(mx, my, bx, by, mw, ml, bw, bl):
    if mx > bx - mw and mx < bx + bw:
        if my > by - ml and my < by + bl:
            return True
    return False

def rectExpand(rect):
    if rect[5] < 300:
        rect[5] += 2
    if rect[6] < 300:
        rect[6] += 2
    rect[7] = 40
    if not rect[8] == 1:
        riseSound.play()
        rect[8] = 1
    
def rectSmall(rect):
    if rect[5] > 10:
        rect[5] -= 2
    if rect[6] > 10:
        rect[6] -= 2
    rect[7] = 0
    if not rect[8] == 2:
        fallSound.play()
        rect[8] = 2
        
def drawbg(x, y, a, b, cx, cy):
    pygame.draw.rect(screen, (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255)), [x, y, a, b], 0)
    if a < 40:
        return
    drawbg(x + 0.13*(cx - x), y + 0.13*(cy - y), (x + a - cx) * 0.87 + cx - x - 0.13*(cx - x), (y + b - cy) * 0.87 + cy - y - 0.13*(cy - y), cx, cy)
        
w = 1080
h = 640
squareW = 40
squareL = 40

white = (255, 255, 255)
pygame.init()
size = (w, h)
aLotOfThings = makeThings(10)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("boring game")
riseSound = pygame.mixer.Sound("rise.ogg")
fallSound = pygame.mixer.Sound("fall.ogg")
run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    cat = pygame.mouse.get_pos()
    drawbg(0, 0, w, h, cat[0] + 20, cat[1] + 20)
    
    collide = False
    small = False
    
    for i in aLotOfThings:
        i[7] -= 1
        if collision(cat[0], cat[1], i[0], i[1], squareW, squareL, i[5], i[6]):
            i[2] = ran.randint(0, 255)
            i[3] = ran.randint(0, 255)
            i[4] = ran.randint(0, 255)
            collide = True
            rectExpand(i)
        elif i[7] < 0:
            i[7] = 0
            rectSmall(i)
            if i[5] > 13:
                i[2] = ran.randint(0, 255)
                i[3] = ran.randint(0, 255)
                i[4] = ran.randint(0, 255)
                small = True
        else:
            i[8] = 0
            
        drawRect(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
    
    if not collide:
        riseSound.stop()
    if not small:
        fallSound.stop()
    
    drawRect(cat[0], cat[1], ran.randint(0, 255), ran.randint(0, 255), ran.randint(0, 255), squareW, squareL)
    
    clock.tick(20)
    pygame.display.flip()

    
pygame.display.quit()
pygame.quit()
os._exit(0)
    
