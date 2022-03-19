import pygame
import random
def attackMovement(attackList,screen,bullet):
    if attackList:
        for attackRect in attackList:
            attackRect.x -= 10
            #screen.fill((0,0,0))
            screen.blit(bullet, attackRect)

        attackList = [attack for attack in attackList if attack.x > -100]
        return attackList
    else:
        return []


