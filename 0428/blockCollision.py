#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import random as ran


class block(pygame.sprite.Sprite):
    def __init__(self, color, w, h):
        super().__init__()
        self.point = w * h / 100
        self.image = pygame.Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def changeColor(self):
        self.image.fill((ran.randrange(255), ran.randrange(255), ran.randrange(255)))

    def fall(self):
        self.rect.y += 2
        if self.rect.y > 640:
            self.rect.y = 0
            self.rect.x = ran.randrange(1080)


def print_text(screen, font, x, y, text):
    imgText = font.render(text, True, (ran.randint(0, 255), ran.randint(0, 255), ran.randint(0, 255)), white)
    screen.blit(imgText, (x, y))


screenW = 1080
screenH = 640
score = 0
sec = 0
screenSize = (screenW, screenH)
allSprite = pygame.sprite.Group()
allBlocks = pygame.sprite.Group()

white = (255, 255, 255)
black = (0, 0, 0)
playerColor = (132, 34, 58)
pygame.init()
font = pygame.font.SysFont('SimHei', 80)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
run = True

for i in range(30):
    addBlock = block(black, ran.randint(15, 35), ran.randint(15, 35))
    addBlock.rect.x = ran.randrange(screenW)
    addBlock.rect.y = ran.randrange(screenH)
    allSprite.add(addBlock)
    allBlocks.add(addBlock)

player = block(playerColor, 20, 20)
allSprite.add(player)
startTime = pygame.time.get_ticks()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(50)

    if (pygame.time.get_ticks() - startTime) / 1000 > 10:
        screen.fill(white)
        allSprite.draw(screen)
        print_text(screen, font, 0, 0, str(round(score, 1)))
        print_text(screen, font, 0, 50, str(sec) + " s")
        print_text(screen, font, 200, 200, "Game over")
        pygame.display.flip()
        continue

    mousePos = pygame.mouse.get_pos()
    player.rect.x = mousePos[0]
    player.rect.y = mousePos[1]

    for blocks in allBlocks.sprites():
        blocks.fall()
        blocks.changeColor()

    sec = round((pygame.time.get_ticks() - startTime) / 1000, 1)

    screen.fill(white)
    allSprite.draw(screen)
    print_text(screen, font, 0, 0, str(round(score, 1)))
    print_text(screen, font, 0, 50, str(sec) + " s")
    collideBlocks = pygame.sprite.spritecollide(player, allBlocks, True)
    for i in collideBlocks:
        score += i.point

    pygame.display.flip()

pygame.display.quit()
pygame.quit()
