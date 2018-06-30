import time
import pygame
from pygame.locals import *

lastTime = 0
imageOrigin = [0, 0 ,32 ,32]

def canMove(lastTime):
    currentTime = time.time()
    return currentTime >= lastTime + 0.008
def animationRefresh(x, y, window, playersIMG, xP, yP):
    imageOrigin[0] = x
    imageOrigin[1] = y
    refresh(window, playersIMG, xP, yP, imageOrigin)
def animationChange(x, window, playersIMG, xP, yP):
    pixelInY = [0, 32, 64]
    pixelInX = [0, 32, 64]
    if x == 0:
        for value in pixelInY:
            animationRefresh(0, value, window, playersIMG, xP, yP)
            yP += 2
    elif x == 1:
        for value in pixelInX:
            animationRefresh(32, value, window, playersIMG, xP, yP)
            xP += 2
    elif x == 2:
        for value in pixelInY:
            animationRefresh(64, value, window, playersIMG, xP, yP)
            yP -= 2
    elif x == 3:
        for value in pixelInX:
            animationRefresh(96, value, window, playersIMG, xP, yP)
            xP -= 2
    return xP, yP

def animationPlayers(keys, window, playersIMG, xP, yP):
    if keys == K_DOWN:
        xP, yP = animationChange(0, window, playersIMG, xP, yP)
    elif keys == K_UP:
        xP, yP = animationChange(2, window, playersIMG, xP, yP)
    elif keys == K_RIGHT :
        xP, yP = animationChange(1, window, playersIMG, xP, yP)
    elif keys == K_LEFT:
        xP, yP = animationChange(3, window, playersIMG, xP, yP)
    else:
        refresh(window, playersIMG, xP, yP, imageOrigin)

    return xP, yP

def refresh(window, playerIMG, xP, yP, animation):
    window.fill((255, 255, 255))
    window.blit(playerIMG, (xP, yP), animation)
    pygame.display.flip()

def move(keys,window, playersIMG, xP, yP ):
    global lastTime
    if  canMove(lastTime):
        xP, yP = animationPlayers(keys, window, playersIMG, xP, yP)
        lastTime = time.time()
    return xP, yP

def checkKeys():
    movement_keys = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
    keys_pressed = pygame.key.get_pressed()
    for key in movement_keys:
        if keys_pressed[key]:
            return key

