import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Match the icons")

font = pygame.font.SysFont("Arial", 90)
heading = font.render("Match the icons!", 1, (0, 0, 0))
subway_surfers_text = font.render("Subway Surfers", 1, (0, 0, 0))
ludo_text = font.render("Ludo", 1, (0, 0, 0))
candy_crush_text = font.render("Candy Crush", 1, (0, 0, 0))
temple_run_text = font.render("Temple Run", 1, (0, 0, 0))

subway_surfers = pygame.image.load("Python_Pro_Game_Dev/match/subway_surfers.png")
ludo = pygame.image.load("Python_Pro_Game_Dev/match/ludo.png")
candy_crush = pygame.image.load("Python_Pro_Game_Dev/match/candy_crush.jpg")
temple_run = pygame.image.load("Python_Pro_Game_Dev/match/temple_run.png")

def draw_apps():
    screen.blit(subway_surfers, (100, 248))
    screen.blit(ludo, (100, 386))
    screen.blit(candy_crush, (100, 524))
    screen.blit(temple_run, (100, 672))

    screen.blit(temple_run_text, (300, 248))
    screen.blit(candy_crush_text, (300, 386))
    screen.blit(subway_surfers_text, (300, 524))
    screen.blit(ludo_text, (300, 672))

    screen.blit(heading, (100, 90))

clicked = False

last_pos = ()
lines = []

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clicked:
                lines.append((last_pos, pygame.mouse.get_pos()))
            else:
                last_pos = pygame.mouse.get_pos()
            clicked = not clicked
    draw_apps()
    for i in lines:
        pygame.draw.circle(screen, (0, 0, 0), i[0], 5)
        pygame.draw.circle(screen, (0, 0, 0), i[1], 5)
        pygame.draw.aaline(screen, (0, 0, 0), i[0], i[1])
    pygame.display.flip()