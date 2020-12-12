import pygame,sys 
from pygame.locals import *
from random  import randint

pygame.init()
ventana = pygame.display.set_mode((600,400))
pygame.display.set_caption("Hola mundo")

imagenGoku = pygame.image.load("C:/Users/JorgeRomero/Desktop/imagenes/goku.png")
posX = randint(1,200)
posY = randint(1,100)

velocidad = 1
blanco = (0,0,13)
derecha = True

while True:  
    ventana.fill(blanco)
    ventana.blit(imagenGoku,(posX,posY))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    if derecha == True:
        if posX < 400 :
            posX += velocidad
        else:
            derecha = False  
    else:
        if posX > 1 :
            posX -= velocidad
        else:
            derecha = True  


    pygame.display.update()