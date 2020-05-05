#!/usr/bin/env python
# coding: utf-8
#today

import pygame as pg, random, math, time


class Ball(pg.sprite.Sprite):
    dx = 0
    dy = 0
    x = 0
    y = 0
    direction = 0
    speed = 0

    def __init__(self, sp, x, y, radium, color):
        pg.sprite.Sprite.__init__(self)
        self.speed = sp
        self.startSpeed = sp
        self.x = x
        self.y = y
        self.r = radium
        self.image = pg.Surface([radium * 2, radium * 2], pg.SRCALPHA)
        self.image.fill((255, 255, 255, 0))
        pg.draw.circle(self.image, color, (radium, radium), radium, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = random.randint(40, 70)

    def update(self):
        radian = math.radians(self.direction)
        self.dx = self.speed * math.cos(radian)
        self.dy = -self.speed * math.sin(radian)
        self.x += self.dx
        self.y += self.dy
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        if (self.rect.left <= 0 or self.rect.right >= screen.get_width() - 10):
            self.bouncelr()
        elif (self.rect.top < 10):
            self.rect.top = 10
            self.bouncedown()
        if (self.rect.bottom >= screen.get_height() - 10):
            return True
        else:
            return False

    def flash(self):
        pg.draw.circle(self.image, (random.randrange(255), random.randrange(255), random.randrange(255)), (self.r, self.r), self.r, 0)

    def bounceup(self):
        if self.direction > 180:
            self.direction = 360 - self.direction

    def bouncedown(self):
        if self.direction < 180:
            self.direction = 360 - self.direction

    def bouncelr(self):
        self.direction = (180 - self.direction) % 360


class Brick(pg.sprite.Sprite):
    def __init__(self, color, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([38, 13])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Pad(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.width = 200
        self.image = pg.Surface([self.width, 10])
        self.color = (random.randrange(255), random.randrange(255), random.randrange(255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width) / 2)
        self.rect.y = screen.get_height() - self.rect.height - 30

    def update(self):
        self.image = pg.transform.scale(self.image, (round(self.width), 10))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width) / 2)
        self.rect.y = screen.get_height() - self.rect.height - 30
        pos = pg.mouse.get_pos()
        self.rect.x = pos[0] - int(self.rect.width / 2)
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0


# 結束程式
def gameover(message):
    global endMessage
    endMessage = message
    text = ffont.render(message, 1, (255, 0, 255))
    screen.blit(text, (int(screen.get_width() / 2) - 150, int(screen.get_height() / 2) - 20))
    pg.display.update()


pg.init()
score = 0
dfont = pg.font.SysFont("Arial", 20)
ffont = pg.font.SysFont("SimHei", 32)
#soundhit = pg.mixer.Sound("media\\hit.wav")
#soundpad = pg.mixer.Sound("media\\pad.wav")
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("wejifnweijfnjisd")
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
allsprite = pg.sprite.Group()
bricks = pg.sprite.Group()
balls = pg.sprite.Group()
for i in range(1):
    startSpeed = random.randrange(3,9)
    ball = Ball(startSpeed, random.randint(50, 500), 300, 10, (0, 0, 0, 0))
    allsprite.add(ball)
    balls.add(ball)
pad = Pad()
allsprite.add(pad)
bounced = 0
addBall = 100
endMessage = ""
reduceWidth = 0

for row in range(0, 5):
    for column in range(0, 15):
        brick = Brick((random.randrange(255), random.randrange(255), random.randrange(255)), column * 40 + 1, row * 15 + 1)
        bricks.add(brick)
        allsprite.add(brick)

clock = pg.time.Clock()
downmsg = "Press Left Click Button to start game"
playing = False
running = True
gameEnd = False

# 運行的程式碼
while running:
    clock.tick(40)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if gameEnd:
        text = ffont.render(endMessage, 1, (255, 0, 255))
        screen.blit(text, (int(screen.get_width() / 2) - 150, int(screen.get_height() / 2) - 20))
        message = dfont.render(downmsg, 1, (255, 0, 255))
        screen.blit(message, (int(screen.get_width() / 2) - 125, screen.get_height() - 30))
        pg.display.update()
        continue

    buttons = pg.mouse.get_pressed()
    if buttons[0]:
        playing = True
        startTime = pg.time.get_ticks()


    if playing == True:
        screen.blit(background, (0, 0))
        addBall = max(addBall - 1, 0)
        if math.floor((pg.time.get_ticks() - startTime) / 1000) % 4 == 0 and addBall == 0:
            startSpeed = random.randrange(3, 9)
            ball = Ball(startSpeed, pad.rect.x + int(pad.rect.width / 2), 300, 10, (0, 0, 0))
            ball.flash()
            allsprite.add(ball)
            balls.add(ball)
            addBall = 100
        for ball in balls:
            ball.speed = ball.startSpeed * ((pg.time.get_ticks() - startTime + 40000) / 40000)
            ball.flash()
            fail = ball.update()
            if fail:
                score -= 2
                balls.remove(ball)
                allsprite.remove(ball)
        if len(balls) == 0:
            gameover("You lose")
            playing = False
        pad.update()
        reduceWidth = max(reduceWidth - 1, 0)
        if math.floor((pg.time.get_ticks() - startTime) / 100) % 1 == 0 and reduceWidth == 0:
            if pad.width > 20:
                pad.width -= 0.4
            reduceWidth = 2
        hit = pg.sprite.groupcollide(balls, bricks, False, True)
        for hitBalls, hitBricks in hit.items():
            score += len(hitBricks)
            #soundhit.play()
            hitBalls.bouncedown()
        if len(bricks) == 0:
            gameover("You win")
            playing = False
        hitpad = pg.sprite.spritecollide(pad, balls, False)
        for ball in hitpad:
            #soundpad.play()
            ball.bounceup()
        allsprite.draw(screen)
        timeNow = round((pg.time.get_ticks() - startTime) / 1000, 1)
        downmsg = "Score: " + str(score) + " Time: " + str(timeNow)
    message = dfont.render(downmsg, 1, (255, 0, 255))
    screen.blit(message, (int(screen.get_width() / 2) - 125, screen.get_height() - 30))
    pg.display.update()
pg.quit()