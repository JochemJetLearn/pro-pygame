import pygame, random

pygame.init()

WIDTH, HEIGHT = 864, 768
CAPTION = "Flappy Bird"
FPS = 60

scrollspeed = 1
jump_power = 15
gravity = 1
max_fall_speed = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

scroll = 0

bg = pygame.image.load("Python_Pro_Game_Dev/flappy_bird/bg.png")
ground = pygame.image.load("Python_Pro_Game_Dev/flappy_bird/ground.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1, 4):
            image = pygame.image.load(f"Python_Pro_Game_Dev/flappy_bird/bird{i}.png")
            self.images.append(image)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 0

    def update(self):
        self.counter += 1
        if self.counter > 5:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
                self.image = self.images[self.index]

        self.velocity -= 1
        if self.velocity < -20:
            self.velocity = -20
        self.rect.y -= self.velocity

    def flap(self):
        self.velocity = jump_power

bird_group = pygame.sprite.Group()

flappy_bird = Bird(100, 300)

bird_group.add(flappy_bird)

def main():
    global scroll
    while True:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                flappy_bird.flap()
        scroll += scrollspeed
        if scroll > ground.get_width():
            scroll = 0
        screen.blit(bg, (0, 0))
        
        bird_group.update()
        bird_group.draw(screen)

        screen.blit(ground, (-scroll, HEIGHT-ground.get_height()))
        screen.blit(ground, (ground.get_width()-scroll, HEIGHT-ground.get_height()))
        
        pygame.display.flip()

main()