#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:40:54 2020

@author: fdbfvuie
"""

import pygame
import random
import os
import math

black = (0, 0, 0)
white = (255, 255, 255)
w = 960
h = 540
mouseDown = False
pygame.init()
font1 = pygame.font.SysFont('SimHei', 24)
size = (w, h)
limit = 30
aPlaceToStorePygameMouseExplodeRadiusVaribleAndHasAVeryLongName = 1
explode = False
pygame.mixer.music.load("no.mp3")
pygame.mixer.music.play()
pos = [[random.randint(0, w), random.randint(0, h)], [random.randint(0, w), random.randint(0, h)]]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("moving circle")

def drawcircle(x, y, r):
    pygame.draw.circle(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (x,y), r, 0)
    
def drawrect(x, y, a, b, cx, cy):
    pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), [x, y, a, b], 0)
    if a < 10:
        return
    drawrect(x + 0.11*(cx - x), y + 0.11*(cy - y), (x + a - cx) * 0.89 + cx - x - 0.11*(cx - x), (y + b - cy) * 0.89 + cy - y - 0.11*(cy - y), cx, cy)
    
def print_text(screen, font, x, y, text):
    imgText = font.render(text, True, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    screen.blit(imgText, (x, y))
    
def mouseExplode(pos, r):
    drawcircle(pos[0], pos[1], r)
    
run = True
while run:
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pos[0][0] -= 6            
    elif keys[pygame.K_RIGHT]:
        pos[0][0] += 6
    elif keys[pygame.K_UP]:
        pos[0][1] -= 6
    elif keys[pygame.K_DOWN]:
        pos[0][1] += 6
    if keys[pygame.K_w]:
        pos[1][1] -= 6            
    elif keys[pygame.K_a]:
        pos[1][0] -= 6
    elif keys[pygame.K_s]:
        pos[1][1] += 6
    elif keys[pygame.K_d]:
        pos[1][0] += 6
    
    if math.sqrt(abs(pos[1][1] - pos[0][1]) ** 2 + abs(pos[1][0] - pos[0][0]) ** 2) < 80:
        drawrect(0, 0, w, h, (pos[0][0] + pos[1][0]) / 2, (pos[0][1] + pos[1][1]) / 2)
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
        screen.fill(white)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
            explode = True
            aPlaceToStorePygameMousePositionVaribleAndHasAVeryLongName = pygame.mouse.get_pos()
            aPlaceToStorePygameMouseExplodeRadiusVaribleAndHasAVeryLongName = 1
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
    
    if mouseDown:
        print_text(screen, font1, pos[0][0] - 35, pos[0][1] - 60, str(pos[0][0]) + " , " + str(pos[0][1]))
        print_text(screen, font1, pos[1][0] - 35, pos[1][1] - 60, str(pos[1][0]) + " , " + str(pos[1][1]))
        
    if explode:
        mouseExplode(aPlaceToStorePygameMousePositionVaribleAndHasAVeryLongName, aPlaceToStorePygameMouseExplodeRadiusVaribleAndHasAVeryLongName)
        aPlaceToStorePygameMouseExplodeRadiusVaribleAndHasAVeryLongName += 5
        if aPlaceToStorePygameMouseExplodeRadiusVaribleAndHasAVeryLongName > limit:
            aPlaceToStorePygameMouseExplodeRadiusVaribleAndHasAVeryLongName = 1
            explode = False
    
    for i in range(len(pos)):
        if pos[i][0] < 0:
            pos[i][0] = w - 40
        elif pos[i][0] > w - 40:
            pos[i][0] = 0
    
        if pos[i][1] < 0:
            pos[i][1] = h - 40
        elif pos[i][1] > h - 40:
            pos[i][1] = 0
            
        r = 40
        while True:  
            drawcircle(pos[i][0], pos[i][1], r)
            r -= 5
            if r < 5:
                break
    
    pygame.display.flip()

    
pygame.display.quit()
pygame.quit()
os._exit(0)
