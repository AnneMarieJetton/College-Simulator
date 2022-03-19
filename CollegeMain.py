# main file

import pygame
import sys
import random
from functions import enemyFunctions
from functions import attackFunctions



pygame.init()

size = (800, 600)

BACKGROUND_COLOR = (0, 0, 0)

screen = pygame.display.set_mode(size)
done = False
x = 50
y = 275
player_surf = pygame.image.load("Assets/Sprites/TestPlayer.png")
player_rect = player_surf.get_rect(center = (x,y))

attack_surf = pygame.image.load("Assets/Sprites/PelletAttackTest.png")

clock = pygame.time.Clock()
fps = 25

width = 40
height = 60
vel = 5

level = 1
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,1)
attackList = []

playerHealth = 1000

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if len(attackList) != 0:
        if keys[pygame.K_LEFT]:
            player_rect.x -= vel
        if keys[pygame.K_RIGHT]:
            player_rect.x += vel
        if keys[pygame.K_UP]:
            player_rect.y -= vel
        if keys[pygame.K_DOWN]:
            player_rect.y += vel


    screen.fill(BACKGROUND_COLOR)

    if event.type == timer:
        delay = random.random()
        if delay < .1:
            attackList.append(attack_surf.get_rect(center = (random.randint(900,1100),random.randint(0,600))))

    screen.blit(player_surf,player_rect)
    enemyFunctions.generateEnemy(screen)
    attackFunctions.attackMovement(attackList,screen,attack_surf)


    pygame.display.update()
    clock.tick(30)

    playerHealth = attackFunctions.collisions(player_rect, attackList, playerHealth)
pygame.quit()