import pygame, sys
from pygame.locals import *
import Players

pygame.init()

width = 1920
height = 1080


xP = 10
yP = 7
window = pygame.display.set_mode((width, height))

window.fill((255, 255, 255))

playerIMG = pygame.image.load("./image/player1.png").convert_alpha()
window.blit(playerIMG, (xP, yP), (0,0,32,32))

pygame.display.flip()

continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
            pygame.quit()
    keys = Players.checkKeys()
    xP, yP = Players.move(keys, window, playerIMG, xP, yP)
