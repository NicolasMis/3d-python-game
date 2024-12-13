import pygame 
import pyopenxr as xr

pygame.init()

screen_width = 800
screen_length = 600

screen = pygame.display.set_mode((screen_width, screen_length))

run= True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
