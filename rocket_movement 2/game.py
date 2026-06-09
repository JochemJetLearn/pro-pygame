import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

spacebg = pygame.image.load("Python_Pro_Game_Dev/rocket_movement/SpaceBg.png")\

rocketx = 600
rockety = 400
rocket = pygame.image.load("Python_Pro_Game_Dev/rocket_movement/rocket.png")

keys = [False, False, False, False]

running = True

while running:
    dt = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            if event.key == K_DOWN:
                keys[1] = True
            if event.key == K_RIGHT:
                keys[2] = True
            if event.key == K_LEFT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0] = False
            if event.key == K_DOWN:
                keys[1] = False
            if event.key == K_RIGHT:
                keys[2] = False
            if event.key == K_LEFT:
                keys[3] = False
    screen.blit(spacebg, (0, 0))

    rockety += dt/10
    if keys[0]:
        rockety -= dt/5
    if keys[1]:
        rockety += dt/5
    if keys[2]:
        rocketx += dt/5
    if keys[3]:
        rocketx -= dt/5
    
    if rockety > 800:
        running = False
    screen.blit(rocket, (rocketx, rockety))
    pygame.display.flip()
