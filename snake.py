import pygame, random
from queue import Queue

snakeWidth = 48
snakeHeight = 48
margin = 2
dx = 1
dy = 0
score = 0
clockTickTime = 5


class segment(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface([snakeWidth, snakeHeight])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x * (snakeWidth + margin)
        self.rect.y = self.y * (snakeHeight + margin)


def newApple(color):
    spawnSpot = appleSpot[random.randrange(len(appleSpot))]
    appleSpot.remove(spawnSpot)
    return segment(color, spawnSpot[0], spawnSpot[1])


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("wejifnweijfnjisd")
appleSpot = []
for i in range(16):
    for j in range(12):
        appleSpot.append([i, j])

snake = []
snakeHead = [0, 0]
allSprite = pygame.sprite.Group()
for i in range(5):
    x = 5 + i
    y = 5
    newSegment = segment((random.randrange(255), random.randrange(255), random.randrange(255)), x, y)
    snake.append(newSegment)
    allSprite.add(newSegment)
    snakeHead = [x, y]
    appleSpot.remove(snakeHead)

redApple = newApple((255, 0, 0))
allSprite.add(redApple)

yellowApple = newApple((255, 255, 0))
allSprite.add(yellowApple)

greenApple = newApple((0, 255, 0))
allSprite.add(greenApple)

blueApple = newApple((0, 0, 255))
allSprite.add(blueApple)

running = True
eatRedApple = False
eatYellowApple = 0
eatGreenApple = False
eatBlueApple = False

while running:
    clock.tick(clockTickTime)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx = 0
                dy = -1
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 1
            elif event.key == pygame.K_LEFT:
                dx = -1
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = 1
                dy = 0

    if snakeHead == [redApple.x, redApple.y]:
        eatRedApple = True

    if snakeHead == [yellowApple.x, yellowApple.y]:
        eatYellowApple = 2

    if snakeHead == [greenApple.x, greenApple.y]:
        eatGreenApple = True

    if snakeHead == [blueApple.x, blueApple.y]:
        eatBlueApple = True

    if not eatRedApple and eatYellowApple == 0:
        removeSnake = snake.pop(0)
        allSprite.remove(removeSnake)
        appleSpot.append([removeSnake.x, removeSnake.y])
    if eatRedApple:
        allSprite.remove(redApple)
        redApple = newApple((255, 0, 0))
        allSprite.add(redApple)
        eatRedApple = False
    if eatYellowApple != 0:
        if eatYellowApple == 1:
            allSprite.remove(yellowApple)
            yellowApple = newApple((255, 255, 0))
            allSprite.add(yellowApple)
        eatYellowApple -= 1
    if eatGreenApple:
        allSprite.remove(greenApple)
        greenApple = newApple((0, 255, 0))
        allSprite.add(greenApple)
        clockTickTime += 1
        eatGreenApple = False
    if eatBlueApple:
        allSprite.remove(blueApple)
        blueApple = newApple((0, 0, 255))
        allSprite.add(blueApple)
        clockTickTime = max(clockTickTime - 1, 1)
        eatBlueApple = False

    snakeHead = [snakeHead[0] + dx, snakeHead[1] + dy]
    for snakeSegment in snake:
        if snakeHead == [snakeSegment.x, snakeSegment.y]:
            running = False
    newSegment = segment((random.randrange(255), random.randrange(255), random.randrange(255)), snakeHead[0],
                         snakeHead[1])
    snake.append(newSegment)
    allSprite.add(newSegment)
    if snakeHead in appleSpot:
        appleSpot.remove(snakeHead)

    if snakeHead[0] >= 16 or snakeHead[0] < 0 or snakeHead[1] >= 12 or snakeHead[1] < 0:
        running = False

    score += len(snake) * clockTickTime

    screen.fill((0, 0, 0))
    allSprite.draw(screen)
    pygame.display.set_caption("wejifnweijfnjisd    Score: " + str(score))
    pygame.display.flip()

pygame.quit()
