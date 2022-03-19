import pygame


def generateEnemy(screen):
    #pygame.draw.rect(screen, (0, 255, 0), (700, 275, 40, 60))
    enemy_surf = pygame.transform.scale2x(pygame.image.load("Assets/Sprites/Enemy.png.png"))
    enemy_rect = enemy_surf.get_rect(center = (700,275))
    screen.blit(enemy_surf,enemy_rect)