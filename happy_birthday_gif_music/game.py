import pygame, time

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Happy Birthday GIF")

font = pygame.font.SysFont("Arial", 50)
song = pygame.mixer.Sound("Python_Pro_Game_Dev/happy_birthday_gif_music/music.mp3")

image1 = pygame.image.load("Python_Pro_Game_Dev/happy_birthday_gif/image1.jpg")
text1 = font.render("Happy Birthday!", 1, (0, 0, 0))

image2 = pygame.image.load("Python_Pro_Game_Dev/happy_birthday_gif/image2.jpg")
text2 = font.render("Blow the candles!", 1, (0, 0, 0))

image3 = pygame.image.load("Python_Pro_Game_Dev/happy_birthday_gif/image3.jpg")
text3 = font.render("Here is your present!", 1, (0, 0, 0))

song.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(image1, (0, 0))
    screen.blit(text1, (160, 200))
    pygame.display.flip()

    time.sleep(1)
    screen.blit(image2, (0, 0))
    screen.blit(text2, (170, 400))
    pygame.display.flip()
    time.sleep(1)

    screen.blit(image3, (0, 0))
    screen.blit(text3, (190, 200))
    pygame.display.flip()
    time.sleep(1)