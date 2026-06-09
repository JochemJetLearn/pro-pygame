import pygame, gif

pygame.init()
pygame.mixer.init()

bulb_gif = gif.Gif([pygame.image.load("Python_Pro_Game_Dev/gif_lib/pic1.png"), pygame.image.load("Python_Pro_Game_Dev/gif_lib/pic2.png"), pygame.image.load("Python_Pro_Game_Dev/gif_lib/pic3.png")], 1, pygame.mixer.Sound("Python_Pro_Game_Dev/gif_lib/music.mp3")).start()

screen = pygame.display.set_mode((800, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    bulb_gif.draw(screen)
    pygame.display.flip()