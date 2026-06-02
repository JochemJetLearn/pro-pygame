import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))

class Circle:
    def __init__(self, surface, pos, radius, color, width=0):
        self.surface = surface
        self.pos = pos
        self.radius = radius
        self.color = color
        self.width = width

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)

blue_circle = Circle(screen, (300, 400), 50, "blue", 10)
yellow_circle = Circle(screen, (350, 450), 50, "yellow", 10)
black_circle = Circle(screen, (400, 400), 50, "black", 10)
green_circle = Circle(screen, (450, 450), 50, "green", 10)
red_circle = Circle(screen, (500, 400), 50, "red", 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill((255, 255, 255))
    blue_circle.draw()
    yellow_circle.draw()
    black_circle.draw()
    green_circle.draw()
    red_circle.draw()
    pygame.display.flip()
