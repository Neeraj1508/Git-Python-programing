# t# displaying the scary prank

import pygame
from time import sleep
pygame.init()
Window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('# their we use scary audio file')
pygame.mixer.music.play()
sleep(4)
pygame.mixer.music.load('# their we use scary audio file which come when pic show')
pygame.mixer.music.play()
sleep(3)
image = pygame.image.load('# scary image')
Window.blit(image, (0,0))
pygame.display.update()
sleep(3)