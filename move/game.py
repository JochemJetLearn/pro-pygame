import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Move Objects")

car = pygame.image.load("Python_Pro_Game_Dev/move/car.png")
car_x = 200
car_y = 300
plane = pygame.image.load("Python_Pro_Game_Dev/move/plane.png")
plane_x = 600
plane_y = 300
bg = pygame.image.load("Python_Pro_Game_Dev/move/bg.png")

while True:
    screen.blit(bg, (0, 0))
    screen.blit(car, (car_x, car_y))
    screen.blit(plane, (plane_x, plane_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.flip()