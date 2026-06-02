import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.lock()
clock = pygame.time.Clock()

class Rectangle:
    def __init__(self, size, color, pos):
        self.color = color
        self.pos = pos
        self.size = size
        self.screen = screen
        self.rect = pygame.Rect(self.pos, (self.size, self.size))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def grow(self, diff):
        self.size += diff
        self.rect.size = (self.size, self.size)
        self.rect.center = self.pos
    
    def update(self):
        self.rect.center = self.pos
        self.rect.size = (self.size, self.size)

def movement(dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        growing_rectangle.pos = (growing_rectangle.pos[0], growing_rectangle.pos[1] - 200 * dt / 1000)
    if keys[pygame.K_s]:
        growing_rectangle.pos = (growing_rectangle.pos[0], growing_rectangle.pos[1] + 200 * dt / 1000)
    if keys[pygame.K_a]:
        growing_rectangle.pos = (growing_rectangle.pos[0] - 200 * dt / 1000, growing_rectangle.pos[1])
    if keys[pygame.K_d]:
        growing_rectangle.pos = (growing_rectangle.pos[0] + 200 * dt / 1000, growing_rectangle.pos[1])

growing_rectangle = Rectangle(5, "green", (400, 400))
last_pos = pygame.mouse.get_pos()
line = []

screen.fill((255, 255, 255))
while True:
    screen.fill((255, 255, 255))
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            growing_rectangle.grow(5)
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            line.append(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                line = []
                growing_rectangle.size = 5
    if len(line) > 1:
        for i in range(len(line) - 1):
            age = len(line) - i
            if age < 60:
                brightness = age * 255 // 60
                color = (brightness, brightness, brightness)
                pygame.draw.line(screen, color, line[i], line[i + 1])
    movement(dt)
    growing_rectangle.update()
    growing_rectangle.draw()
    pygame.display.flip()