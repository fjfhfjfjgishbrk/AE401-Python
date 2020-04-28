{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pygame 1.9.6\n",
      "Hello from the pygame community. https://www.pygame.org/contribute.html\n"
     ]
    }
   ],
   "source": [
    "import pygame\n",
    "import random as ran\n",
    "import os\n",
    "\n",
    "class block(pygame.sprite.Sprite):\n",
    "    def __init__(self, color, w, h):\n",
    "        super().__init__()\n",
    "        self.image = pygame.Surface([w, h])\n",
    "        self.image.fill(color)\n",
    "        self.rect = self.image.get_rect()\n",
    "        \n",
    "    def fall(self):\n",
    "        self.rect.y += 2\n",
    "        if self.rect.y > 640:\n",
    "            self.rect.y = 0\n",
    "            self.rect.x = ran.randrange(1080)\n",
    "\n",
    "def print_text(screen, font, x, y, text):\n",
    "    imgText = font.render(text, True, (ran.randint(0,255), ran.randint(0,255), ran.randint(0,255)), white)\n",
    "    screen.blit(imgText, (x, y))\n",
    "\n",
    "screenW = 1080\n",
    "screenH = 640\n",
    "score = 0\n",
    "sec = 0\n",
    "screenSize = (screenW, screenH)\n",
    "allSprite = pygame.sprite.Group()\n",
    "allBlocks = pygame.sprite.Group()\n",
    "\n",
    "white = (255, 255, 255)\n",
    "black = (0, 0, 0)\n",
    "playerColor = (132, 34, 58)\n",
    "pygame.init()\n",
    "font = pygame.font.SysFont('SimHei', 80)\n",
    "screen = pygame.display.set_mode(screenSize)\n",
    "clock = pygame.time.Clock()\n",
    "run = True\n",
    "\n",
    "for i in range(30):\n",
    "    addBlock = block(black, 20, 20)\n",
    "    addBlock.rect.x = ran.randrange(screenW)\n",
    "    addBlock.rect.y = ran.randrange(screenH)\n",
    "    allSprite.add(addBlock)\n",
    "    allBlocks.add(addBlock)\n",
    "    \n",
    "player = block(playerColor, 20, 20)\n",
    "allSprite.add(player)\n",
    "startTime = pygame.time.get_ticks()\n",
    "\n",
    "while run:\n",
    "    for event in pygame.event.get():\n",
    "        if event.type == pygame.QUIT:\n",
    "            run = False\n",
    "    \n",
    "    if (pygame.time.get_ticks() - startTime) / 1000 > 10:\n",
    "        screen.fill(white)\n",
    "        allSprite.draw(screen)\n",
    "        print_text(screen, font, 0, 0, str(score))\n",
    "        print_text(screen, font, 0, 50, str(sec) + \" s\")\n",
    "        print_text(screen, font, 200, 200, \"Game over\")\n",
    "        pygame.display.flip()\n",
    "        continue\n",
    "    \n",
    "    mousePos = pygame.mouse.get_pos()\n",
    "    player.rect.x = mousePos[0]\n",
    "    player.rect.y = mousePos[1]\n",
    "    \n",
    "    for blocks in allBlocks.sprites():\n",
    "        blocks.fall()\n",
    "    \n",
    "    sec = round((pygame.time.get_ticks() - startTime) / 1000, 1)\n",
    "    \n",
    "    screen.fill(white)\n",
    "    allSprite.draw(screen)\n",
    "    print_text(screen, font, 0, 0, str(score))\n",
    "    print_text(screen, font, 0, 50, str(sec) + \" s\")\n",
    "    collideBlocks = pygame.sprite.spritecollide(player, allBlocks, True)\n",
    "    for i in collideBlocks:\n",
    "        score += 1\n",
    "        \n",
    "    pygame.display.flip()\n",
    "            \n",
    "            \n",
    "\n",
    "\n",
    "pygame.display.quit()\n",
    "pygame.quit()\n",
    "os._exit(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}