import pygame
import random

def generateEnemy(screen):

    #text picking.
    textList = ["Talk to your Ducky", "Eval is Evil"]

    font = pygame.font.Font('Assets/Fonts/Pixeltype.ttf', 30)
    enemy_surf = pygame.transform.scale2x(pygame.image.load("Assets/Sprites/pixil-frame-0.png")).convert_alpha()
    enemy_rect = enemy_surf.get_rect(center = (700,275))
    enemy_speech = font.render(str(textList[0]),False,(225,225,225))

    enemy_speech_rect = enemy_speech.get_rect(center = (700,200))
    screen.blit(enemy_surf,enemy_rect)
    screen.blit(enemy_speech,enemy_speech_rect)