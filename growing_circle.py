import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))


class Circle:
    def __init__(self, radius, color, pos, width):
        self.radius = radius
        self.color = color
        self.pos = pos
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)

    def grow(self, r):
        self.radius += r
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)

growing_circle = Circle(5, "green", (400, 400), 0)
last_pos = pygame.mouse.get_pos()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0, 0, 0))
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255, 255, 255))
            growing_circle.grow(5)
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, "black", pos, last_pos)
            last_pos = pos
            black_circle = Circle(1, "black", pos, 0)
            black_circle.draw()
    
    growing_circle.draw()
    pygame.display.flip()