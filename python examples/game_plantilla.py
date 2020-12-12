import pygame,sys 
from pygame.locals import *
from random  import randint

pygame.init()
ventana = pygame.display.set_mode((600,300))
pygame.display.set_caption("Hola mundo")

while True:  
    for evt in pygame.event.get():
        if evt.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()