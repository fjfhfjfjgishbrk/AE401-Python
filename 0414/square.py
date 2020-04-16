import pygame
import random
import os

black = (0, 0, 0)
white = (255, 255, 255)
pygame.init()
size = (960, 540)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my game")

def drawrect(x, y, l, w):
    pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), [x, y, l, w], 0)
    if l < 6:
        return
    drawrect(x + 0.05*l, y + 0.05*w, l * 0.9, w * 0.9)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    
    screen.fill(white)
    drawrect(0, 0, 960, 540)
    pygame.display.flip()

    
pygame.display.quit()
pygame.quit()
os._exit(0)