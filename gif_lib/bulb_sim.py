import pygame, gif

pygame.init()
pygame.mixer.init()

bulb_gif = gif.Gif([pygame.image.load("Python_Pro_Game_Dev/gif_lib/bulb_off.jpg"), pygame.image.load("Python_Pro_Game_Dev/gif_lib/bulb_on.jpg")]).start()

screen = pygame.display.set_mode((612, 980))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    bulb_gif.draw(screen)
    pygame.display.flip()