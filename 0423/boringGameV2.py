#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:04:06 2020

@author: fdbfvuie
"""


import pygame
import random as ran
import os

def makeThings(count):
    a = []
    for i in range(count):
        #這是註解(x, y, r, g, b, w, l, small time, music, disappear time, point time)
        a.append([ran.randint(0, w - 40), ran.randint(0, h - 40), ran.randint(0, 255), ran.randint(0, 255), ran.randint(0, 255), 40, 40, ran.randint(25, 50), 0, 20, 0])
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
    rect[7] = ran.randint(25, 50)
    if rect[10] < 60:
        rect[10] += 2
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
    
def print_text(screen, font, x, y, text):
    imgText = font.render(text, True, (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255)), white)
    screen.blit(imgText, (x, y))
        
w = 1080
h = 640
squareW = 40
squareL = 40
score = 0

white = (255, 255, 255)
pygame.init()
size = (w, h)
aLotOfThings = makeThings(10)
fontSmall = pygame.font.SysFont('SimHei', 40)
fontBig = pygame.font.SysFont('SimHei', 120)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("boring game")
riseSound = pygame.mixer.Sound("rise.ogg")
fallSound = pygame.mixer.Sound("fall.ogg")
run = True
gameOver = False


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if not gameOver:
        #這是貓咪(老鼠座標)
        cat = pygame.mouse.get_pos()
    drawbg(0, 0, w, h, cat[0] + 20, cat[1] + 20)
    
    collide = False
    small = False
    
    if len(aLotOfThings) == 0:
        print_text(screen, fontBig, 300, 100, "GAME OVER")
        if not gameOver:
            #time
            sec = round(pygame.time.get_ticks() / 1000, 1)
        gameOver = True
    
    for i in aLotOfThings:
        #上面有寫自己看
        i[7] -= 1
        if i[10] > 0:
            i[10] -= 1
        if collision(cat[0], cat[1], i[0], i[1], squareW, squareL, i[5], i[6]):
            i[2] = ran.randint(0, 255)
            i[3] = ran.randint(0, 255)
            i[4] = ran.randint(0, 255)
            i[9] = 20
            collide = True
            score += round(6 - i[10] / 10, 1)
            rectExpand(i)
        elif i[7] < 0:
            i[7] = 0
            rectSmall(i)
            if i[5] > 13:
                i[2] = ran.randint(0, 255)
                i[3] = ran.randint(0, 255)
                i[4] = ran.randint(0, 255)
                i[9] = 20
                small = True
            else:
                i[9] -= 1
        else:
            i[8] = 0
        if i[5] < 40:
            score -= (40 - i[5]) / (20 / sec)
        if i[5] > 200:
            score -= (i[5] - 200) / (20 / sec)
        if i[9] < 0:
            aLotOfThings.remove(i)
            
        drawRect(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
    
    if not collide:
        riseSound.stop()
    if not small:
        fallSound.stop()
    
    drawRect(cat[0], cat[1], ran.randint(0, 255), ran.randint(0, 255), ran.randint(0, 255), squareW, squareL)
    if not gameOver:
        sec = round(pygame.time.get_ticks() / 1000, 1)
        score += len(aLotOfThings) / 2
    if score < 0:
        score = 0
    print_text(screen, fontSmall, 0, 0, str(sec) + " s")
    print_text(screen, fontSmall, 0, 50, "Score: " + str(round(score, 1)))
    
    clock.tick(20)
    pygame.display.flip()

    
pygame.display.quit()
pygame.quit()
os._exit(0)
    