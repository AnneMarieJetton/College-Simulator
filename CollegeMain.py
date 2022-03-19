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
x = 50
y = 275
player_surf = pygame.image.load("Assets/Sprites/TestPlayer.png")
player_rect = player_surf.get_rect(center = (x,y))
clock = pygame.time.Clock()
fps = 25

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
        player_rect.x -= vel
    if keys[pygame.K_RIGHT]:
        player_rect.x += vel
    if keys[pygame.K_UP]:
        player_rect.y -= vel
    if keys[pygame.K_DOWN]:
        player_rect.y += vel
    screen.fill(BACKGROUND_COLOR)

    screen.blit(player_surf,player_rect)
    enemyFunctions.generateEnemy(screen)
    clock.tick(30)

    pygame.display.update()

pygame.quit()