import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont("Arial", 50)

playerspeed = 150
bulletspeed = 250

pygame.display.set_caption("Space Invaders")

bg = pygame.image.load("Python_Pro_Game_Dev/space_invaders 2/bg.png")

red = pygame.image.load("Python_Pro_Game_Dev/space_invaders 2/red.png")
redship = pygame.transform.rotate(pygame.transform.scale(red, (50, 50)), 90)
redhealth = 10

yellow = pygame.image.load("Python_Pro_Game_Dev/space_invaders 2/yellow.png")
yellowship = pygame.transform.rotate(pygame.transform.scale(yellow, (50, 50)), 270)
yellowhealth = 10

yellowrect = pygame.Rect(WIDTH-50, HEIGHT//2, 50, 50)
redrect = pygame.Rect(0, HEIGHT//2, 50, 50)

devider = pygame.Rect(WIDTH//2-10, 0, 20, HEIGHT)

bullets = []

class Bullet:
    def __init__(self, startrect, velocity, color):
        self.velocity = velocity
        self.color = color
        self.startrect = startrect
        if startrect == redrect:
            self.target = yellowrect
        else:
            self.target = redrect
        self.rect = pygame.Rect(startrect.centerx, startrect.centery-5, 20, 10)

    def run(self, dt):
        global redhealth, yellowhealth
        self.rect.x += dt*self.velocity
        pygame.draw.rect(screen, self.color, self.rect)
        if self.rect.colliderect(self.target):
            if self.target == redrect:
                redhealth -= 1
            if self.target == yellowrect:
                yellowhealth -= 1
            return True
        return False

def draw_window(red, yellow):
    screen.blit(bg, (0, 0))
    screen.blit(redship, (red.x, red.y))
    screen.blit(yellowship, (yellow.x, yellow.y))
    pygame.draw.rect(screen, (0, 0, 0), devider)
    redhptext = font.render(f"Red Health: {redhealth}", 1, (255, 255, 255))
    yellowhptext = font.render(f"Yellow Health: {yellowhealth}", 1, (255, 255, 255))
    screen.blit(redhptext, (0, 0))
    screen.blit(yellowhptext, (WIDTH//2, 0))

def movement(dt):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and yellowrect.y > 0:
        yellowrect.y -= dt*playerspeed
    if keys[pygame.K_DOWN] and yellowrect.y < HEIGHT-50:
        yellowrect.y += dt*playerspeed
    if keys[pygame.K_LEFT] and yellowrect.x > WIDTH//2:
        yellowrect.x -= dt*playerspeed
    if keys[pygame.K_RIGHT] and yellowrect.x < WIDTH-50:
        yellowrect.x += dt*playerspeed
    
    
    if keys[pygame.K_w] and redrect.y > 0:
        redrect.y -= dt*playerspeed
    if keys[pygame.K_s] and redrect.y < HEIGHT-50:
        redrect.y += dt*playerspeed
    if keys[pygame.K_a] and redrect.x > 0:
        redrect.x -= dt*playerspeed
    if keys[pygame.K_d] and redrect.x < WIDTH//2-50:
        redrect.x += dt*playerspeed

def main():
    
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    bullets.append(Bullet(redrect, bulletspeed, (255, 0, 0)))
                if event.key == pygame.K_RSHIFT:
                    bullets.append(Bullet(yellowrect, -bulletspeed, (255, 255, 0)))
        movement(dt)
        draw_window(redrect, yellowrect)
        for i in bullets:
            if i.run(dt):
                bullets.remove(i)
        if redhealth <= 0 or yellowhealth <= 0:
            break
        pygame.display.flip()
    if not redhealth <= 0:
        color = (255, 0, 0)
        text = font.render("Red wins!", 1, (0, 0, 0))
    else:
        color = (255, 255, 0)
        text = font.render("Yellow wins!", 1, (0, 0, 0))
    
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return
        screen.fill(color)
        screen.blit(text, (400, 275))
        pygame.display.flip()
        
while True:
    main()
    redhealth = 10
    yellowhealth = 10
    yellowrect = pygame.Rect(WIDTH-50, HEIGHT//2, 50, 50)
    redrect = pygame.Rect(0, HEIGHT//2, 50, 50)
    bullets = []