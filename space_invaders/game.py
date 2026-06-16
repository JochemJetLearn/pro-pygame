import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

playerspeed = 150

pygame.display.set_caption("Space Invaders")

bg = pygame.image.load("Python_Pro_Game_Dev/space_invaders/bg.png")

red = pygame.image.load("Python_Pro_Game_Dev/space_invaders/red.png")
redship = pygame.transform.rotate(pygame.transform.scale(red, (50, 50)), 90)
redhealth = 10

yellow = pygame.image.load("Python_Pro_Game_Dev/space_invaders/yellow.png")
yellowship = pygame.transform.rotate(pygame.transform.scale(yellow, (50, 50)), 270)
yellowhealth = 10

yellowrect = pygame.Rect(WIDTH-50, HEIGHT//2, 50, 50)
redrect = pygame.Rect(0, HEIGHT//2, 50, 50)

devider = pygame.Rect(WIDTH//2-10, 0, 20, HEIGHT)

def draw_window(red, yellow):
    screen.blit(bg, (0, 0))
    screen.blit(redship, (red.x, red.y))
    screen.blit(yellowship, (yellow.x, yellow.y))
    pygame.draw.rect(screen, (0, 0, 0), devider)

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
        movement(dt)
        draw_window(redrect, yellowrect)
        pygame.display.flip()

main()