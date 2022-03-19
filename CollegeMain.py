# main file

import pygame
import sys
import random
from functions import enemyFunctions
from functions import attackFunctions

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('College Simulator')
clock = pygame.time.Clock()
BACKGROUND_COLOR = (0, 0, 0)
fps = 25

width = 40
height = 60
vel = 5

level = 1
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,1)
attackList = []
playerHealth = 50

font = pygame.font.Font("Assets/Fonts/Pixeltype.ttf",75)
gameDone = False

while not gameDone:

    while True:
        event = pygame.event.wait()
        playerHealth = 50
        attackList = []
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:

                # levelDone = False
                break
        else:
            screen.fill((94, 129, 162))
            title_message = font.render("College Simulator", True, (0,0,0))
            title_message_rect = title_message.get_rect(center=(300, 300))
            play_message = font.render("Hit Enter To Play", False, (0,0,0))
            play_message_rect = play_message.get_rect(center = (300,350))
            duckie_menu = pygame.transform.scale(pygame.image.load('Assets/Sprites/duckie3.0.png'),(200,200))
            duckie_menu_rect = duckie_menu.get_rect(center = (400,400))

            screen.blit(title_message, (225, 100))
            screen.blit(play_message,(225,200))
            screen.blit(duckie_menu, duckie_menu_rect)

            pygame.display.update()

    levelDone = False
    numAttacks = 0
    while not levelDone:
        #level loop

        attackDone = False
        x = 50
        y = 275
        player_surf = pygame.image.load("Assets/Sprites/Protagonist2.png").convert_alpha()
        player_rect = player_surf.get_rect(center = (x,y))

        attack_surf = pygame.image.load("Assets/Sprites/BigDuckie.png")

        levelTimer = 20


        while not attackDone:
            #attack loop


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    attackDone = True

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

            if player_rect.y < 0:
                player_rect.y = 0
            if player_rect.y > 575:
                player_rect.y = 575
            if player_rect.x > 600:
                player_rect.x = 600
            if player_rect.x < 0:
                player_rect.x = 0

            screen.fill(BACKGROUND_COLOR)

            if event.type == timer:
                delay = random.random()
                if delay < .1:
                    if levelTimer != 0:
                        attackList.append(attack_surf.get_rect(center = (random.randint(900,1100),random.randint(0,600))))
                        levelTimer = levelTimer - 1
                        # print(len(attackList))
                    else:
                        # print(attackList[len(attackList) - 1].x)
                        if attackList[len(attackList) - 1].x <= 0:
                            attackDone = True

            screen.blit(player_surf,player_rect)
            enemyFunctions.generateEnemy(screen)
            attackFunctions.attackMovement(attackList,screen,attack_surf,)


            pygame.display.update()
            clock.tick(30)

            playerHealth = attackFunctions.collisions(player_rect, attackList, playerHealth)
            if playerHealth <= 0:
                attackDone = True

        numAttacks = numAttacks + 1

        if numAttacks == 4:
            levelDone = True
pygame.quit()