import pygame
from time import sleep as s
pygame.init()
a = pygame.mixer.Sound("assets/music/audio1.mp3")
b = pygame.mixer.Sound("assets/music/audio1.mp3")
a.play(loops=-1)
s(2)
b.play()
while(1):
    pass