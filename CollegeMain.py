# main file

import pygame
import sys
import random

pygame.init()

size = (800, 600)

BACKGROUND_COLOR = (0, 0, 0)

screen = pygame.display.set_mode(size)
done = False

clock = pygame.time.Clock()
fps = 25

while not done:
    screen.fill(BACKGROUND_COLOR)
    clock.tick(30)
    pygame.display.update()

pygame.quit()