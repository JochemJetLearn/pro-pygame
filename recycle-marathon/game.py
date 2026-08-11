import pygame, time, random

pygame.init()

WIDTH, HEIGHT = 1210, 908

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans", 30, True)
bigfont = pygame.font.SysFont("Comic Sans", 60, True)
biggerfont = pygame.font.SysFont("Comic Sans", 120, True)

bg = pygame.image.load("Python_Pro_Game_Dev/recycle-marathon/bg.png")

given_time = 60         # sec
playerspeed = 150       # px/sec
playersize = 70         # player height (px)
trashsize = 40          # items height (px)
total_recycle = 100     # total recycleable items
total_non_recycle = 50  # total non-recycleable items

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Python_Pro_Game_Dev/recycle-marathon/bin.png")
        scale = playersize / self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*scale, self.image.get_height()*scale))
        self.rect = self.image.get_rect()

class Pickup_item(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        scale = trashsize / self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*scale, self.image.get_height()*scale))
        self.rect = self.image.get_rect()

recycleable_img = ["Python_Pro_Game_Dev/recycle-marathon/crate.png", "Python_Pro_Game_Dev/recycle-marathon/paper_bag.png", "Python_Pro_Game_Dev/recycle-marathon/pencil.png"]
non_recycleable_img = ["Python_Pro_Game_Dev/recycle-marathon/plastic_bag.png", "Python_Pro_Game_Dev/recycle-marathon/plastic_container.png"]

bin = Bin()
bin.rect.x = WIDTH // 2
bin.rect.y = HEIGHT // 2
points = 0


all_sprites = pygame.sprite.Group()
recycleable_items = pygame.sprite.Group()
non_recycle_items = pygame.sprite.Group()
def spawn():
    for i in range(total_recycle):
        img = random.choice(recycleable_img)
        item = Pickup_item(img)
        item.rect.x = random.randint(0, WIDTH-item.image.get_width())
        item.rect.y = random.randint(0, HEIGHT-item.image.get_height())
        all_sprites.add(item)
        recycleable_items.add(item)

    for i in range(total_non_recycle):
        img = random.choice(non_recycleable_img)
        item = Pickup_item(img)
        item.rect.x = random.randint(0, WIDTH-item.image.get_width())
        item.rect.y = random.randint(0, HEIGHT-item.image.get_height())
        all_sprites.add(item)
        non_recycle_items.add(item)
spawn()
all_sprites.add(bin)

def movement(dt):
    global points
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        bin.rect.y -= playerspeed*dt
    if keys[pygame.K_s]:
        bin.rect.y += playerspeed*dt
    if keys[pygame.K_a]:
        bin.rect.x -= playerspeed*dt
    if keys[pygame.K_d]:
        bin.rect.x += playerspeed*dt
    
    recycleable = recycleable_items.sprites()
    for i in recycleable:
        if bin.rect.colliderect(i.rect):
            points += 1
            recycleable_items.remove(i)
            all_sprites.remove(i)
    
    non_recycleable = non_recycle_items.sprites()
    for i in non_recycleable:
        if bin.rect.colliderect(i.rect):
            points -= 1
            non_recycle_items.remove(i)
            all_sprites.remove(i)
def main():
    endtime = time.time() + given_time

    while True:
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        if endtime < time.time():
            break
        movement(dt)
        screen.blit(bg, (0, 0))

        all_sprites.draw(screen)
        time_text = font.render(f"Time left: {round(endtime-time.time(), 2)}", 1, (0, 0, 0))
        points_text = font.render(f"Points: {points}", 1, (0, 0, 0))
        screen.blit(time_text, (10, 10))
        screen.blit(points_text, (10, 50))

        pygame.display.flip()
    losetime = time.time()
    wintext = biggerfont.render("GAME!", 1, (0, 0, 0))
    points_text = bigfont.render(f"Points: {points}", 1, (0, 0, 0))
    reset_text = bigfont.render("Press [R] to restart.", 1, (0, 0, 0))
    diff = HEIGHT/2-wintext.get_height()*2+wintext.get_height()
    animtime = 0.15
    while True:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return

        if points > 0:
            screen.fill((0, 255, 0))
        else:
            screen.fill((255, 0, 0))
        currenttime = time.time()
        deathtime = currenttime-losetime
        
        if deathtime > animtime:
            screen.blit(wintext, (WIDTH/2-wintext.get_width()/2, HEIGHT/2-wintext.get_height()*2))
        else:
            screen.blit(wintext, (WIDTH/2-wintext.get_width()/2, -wintext.get_height()+diff*deathtime*(1/animtime)))
        if deathtime > 1:
            screen.blit(points_text, (WIDTH/2-points_text.get_width()/2, HEIGHT/2+points_text.get_height()-50))
        if deathtime > 2:
            screen.blit(reset_text, (WIDTH/2-reset_text.get_width()/2, HEIGHT-reset_text.get_height()-10))

        pygame.display.flip()

while True:
    main()
    points = 0
    bin.rect.x = WIDTH // 2
    bin.rect.y = HEIGHT // 2

    all_sprites = pygame.sprite.Group()
    recycleable_items = pygame.sprite.Group()
    non_recycle_items = pygame.sprite.Group()
    spawn()
    all_sprites.add(bin)