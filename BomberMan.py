import pygame, sys
from pygame.locals import *


pygame.init()

width = 640
height = 480

xP = 10
yP = 7
window = pygame.display.set_mode((width, height))

background = pygame.image.load("background.jpg").convert()
window.blit(background, (0,0))

playerIMG = pygame.image.load("player.png").convert_alpha()
window.blit(playerIMG, (xP, yP))

pygame.display.flip()

continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        elif event.type == KEYDOWN or event.type == KEYUP :
            if event.key == K_UP:
                yP -= 5
            elif event.key == K_DOWN:
                yP += 5
            elif event.key == K_LEFT:
                xP -= 5
            elif event.key == K_RIGHT:
                xP += 5

    window.blit(background, (0,0))
    window.blit(playerIMG, (xP, yP))
    pygame.display.flip()
