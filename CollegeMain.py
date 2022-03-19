# main file

import pygame
import sys
import random
from functions import enemyFunctions



pygame.init()

size = (800, 600)

BACKGROUND_COLOR = (0, 0, 0)

screen = pygame.display.set_mode(size)
done = False

clock = pygame.time.Clock()
fps = 25
x = 50
y = 440
width = 40
height = 60
vel = 5

level = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    enemyFunctions.generateEnemy(screen)
    clock.tick(30)

    pygame.display.update()

pygame.quit()