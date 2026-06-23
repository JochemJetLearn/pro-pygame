import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000, 668))
clock = pygame.time.Clock()

spacebg = pygame.image.load("Python_Pro_Game_Dev/viechles/grassbg.png")\

carx = 600
cary = 400
car = pygame.image.load("Python_Pro_Game_Dev/viechles/car.png")
bikex = 600
bikey = 400
bike = pygame.image.load("Python_Pro_Game_Dev/viechles/bike.png")

def movement(dt):
    global car, carx, cary, bike, bikex, bikey
    keys = pygame.key.get_pressed()

    if keys[K_UP]:
        cary -= dt/5
    if keys[pygame.K_DOWN]:
        cary += dt/5
    if keys[pygame.K_RIGHT]:
        carx += dt/5
    if keys[pygame.K_LEFT]:
        carx -= dt/5
    if keys[K_w]:
        bikey -= dt/5
    if keys[K_s]:
        bikey += dt/5
    if keys[K_d]:
        bikex += dt/5
    if keys[K_a]:
        bikex -= dt/5

running = True

while running:
    dt = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(spacebg, (0, 0))

    movement(dt)
    screen.blit(car, (carx, cary))
    screen.blit(bike, (bikex, bikey))
    pygame.display.flip()
