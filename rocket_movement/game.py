import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

spacebg = pygame.image.load("Python_Pro_Game_Dev/rocket_movement/SpaceBg.png")\

rocketx = 600
rockety = 400
rocket = pygame.image.load("Python_Pro_Game_Dev/rocket_movement/rocket.png")

def movement(dt):
    global rocket, rocketx, rockety, running
    keys = pygame.key.get_pressed()

    rockety += dt/10
    if keys[pygame.K_SPACE] or keys[K_UP]:
        rockety -= dt/5
    if keys[pygame.K_DOWN]:
        rockety += dt/5
    if keys[pygame.K_RIGHT]:
        rocketx += dt/5
    if keys[pygame.K_LEFT]:
        rocketx -= dt/5
    
    if rockety > 800:
        running = False

running = True

while running:
    dt = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(spacebg, (0, 0))

    movement(dt)
    screen.blit(rocket, (rocketx, rockety))
    pygame.display.flip()
