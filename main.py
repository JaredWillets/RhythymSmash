import pygame
from pygame.locals import *

pygame.init()


class game:
    running = True
    resolution = (800, 500)
    screen = pygame.display.set_mode(resolution)
    frame = 0
    keysPressed = {}
    gameBackground = pygame.image.load('background1.png')


class character:
    position = ()
    jumping = False
    timeSinceJump = 0


def checkHitbox():
    print('todo')


projectiles = []

while game.running:
    game.screen.blit(game.gameBackground, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.KEYDOWN:
            game.keysPressed[pygame.key.name(event.key)] = True
        if event.type == pygame.KEYUP:
            game.keysPressed[pygame.key.name(event.key)] = False

	
    pygame.display.update()
    game.frame += 1
pygame.quit()
