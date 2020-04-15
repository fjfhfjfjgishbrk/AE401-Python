#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:08:50 2020

@author: fdbfvuie
"""


import pygame

black = (0, 0, 0)
white = (255, 255, 255)
pygame.init()
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my game")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    
    screen.fill(white)       
    pygame.draw.line(screen, black, (350, 0), (350, 700), 3)
    pygame.draw.line(screen, black, (0, 350), (700, 350), 3)
    pygame.draw.dot(screen, black, (450, 400), 1, 0)
    pygame.display.flip()

pygame.quit()
    

