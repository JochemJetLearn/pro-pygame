import pygame, time, random

pygame.init()

WIDTH, HEIGHT = 1210, 908

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg = pygame.image.load("Python_Pro_Game_Dev/recycle-marathon/bg.png")

playerspeed = 150
playersize = 70
trashsize = 40
total_items = 100

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Python_Pro_Game_Dev/recycle-marathon/bin.png")
        scale = playersize / self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*scale, self.image.get_height()*scale))
        self.rect = self.image.get_rect()

class Recycleable(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        scale = trashsize / self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*scale, self.image.get_height()*scale))
        self.rect = self.image.get_rect()

recycleable_img = ["Python_Pro_Game_Dev/recycle-marathon/crate.png", "Python_Pro_Game_Dev/recycle-marathon/paper_bag.png", "Python_Pro_Game_Dev/recycle-marathon/pencil.png"]

bin = Bin()
bin.rect.x = WIDTH // 2
bin.rect.y = HEIGHT // 2

all_sprites = pygame.sprite.Group()
recycleable_items = pygame.sprite.Group()
non_recycle_items = pygame.sprite.Group()

for i in range(total_items):
    img = random.choice(recycleable_img)
    item = Recycleable(img)
    item.rect.x = random.randint(0, WIDTH-item.image.get_width())
    item.rect.y = random.randint(0, HEIGHT-item.image.get_height())
    all_sprites.add(item)
    recycleable_items.add(item)

all_sprites.add(bin)

def movement(dt):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        bin.rect.y -= playerspeed*dt
    if keys[pygame.K_s]:
        bin.rect.y += playerspeed*dt
    if keys[pygame.K_a]:
        bin.rect.x -= playerspeed*dt
    if keys[pygame.K_d]:
        bin.rect.x += playerspeed*dt

while True:
    dt = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    movement(dt)
    screen.blit(bg, (0, 0))

    all_sprites.draw(screen)

    pygame.display.flip()