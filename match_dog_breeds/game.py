import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Match the dog breeds")

font = pygame.font.SysFont("Arial", 90)
heading = font.render("Match the dog breeds!", 1, (0, 0, 0))
husky_text = font.render("Husky", 1, (0, 0, 0))
german_shepherd_text = font.render("German Shepherd", 1, (0, 0, 0))
bulldog_text = font.render("Bulldog", 1, (0, 0, 0))
golden_retriever_text = font.render("Golden Retriever", 1, (0, 0, 0))

husky = pygame.image.load("Python_Pro_Game_Dev/match_dog_breeds/husky.png")
german_shepherd = pygame.image.load("Python_Pro_Game_Dev/match_dog_breeds/german_shepherd.png")
bulldog = pygame.image.load("Python_Pro_Game_Dev/match_dog_breeds/bulldog.png")
golden_retriever = pygame.image.load("Python_Pro_Game_Dev/match_dog_breeds/golden_retriever.png")

def draw_breeds():
    screen.blit(husky, (100, 248))
    screen.blit(german_shepherd, (100, 386))
    screen.blit(bulldog, (100, 524))
    screen.blit(golden_retriever, (100, 672))

    screen.blit(golden_retriever_text, (300, 248))
    screen.blit(bulldog_text, (300, 386))
    screen.blit(husky_text, (300, 524))
    screen.blit(german_shepherd_text, (300, 672))

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                clicked = False
            if event.key == pygame.K_r:
                lines = []
    draw_breeds()
    for i in lines:
        pygame.draw.circle(screen, (0, 0, 0), i[0], 5)
        pygame.draw.circle(screen, (0, 0, 0), i[1], 5)
        pygame.draw.aaline(screen, (0, 0, 0), i[0], i[1])
    if clicked:
        pygame.draw.aaline(screen, (255, 0, 0), last_pos, pygame.mouse.get_pos())
    pygame.display.flip()