import pygame,sys 
from pygame.locals import *
from random  import randint

pygame.init()
ventana = pygame.display.set_mode((600,400))
pygame.display.set_caption("Hola mundo")

imagenGoku = pygame.image.load("C:/Users/JorgeRomero/Desktop/imagenes/goku.png")
posX = randint(1,200)
posY = randint(1,100)

velocidad = 20
blanco = (0,0,13)
derecha = True

while True:  
    ventana.fill(blanco)
    ventana.blit(imagenGoku,(posX,posY))

    for evt in pygame.event.get():
        if evt.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evt.type == pygame.KEYDOWN:
             if evt.key == K_LEFT:
                 posX -=  velocidad
             elif evt.key == K_RIGHT:
                 posX +=  velocidad 
             elif evt.key == K_UP:
                 posY -=  velocidad 
             elif evt.key == K_DOWN:
                 posY +=  velocidad 
        elif evt.type == pygame.KEYUP:
             if evt.key == K_LEFT:
                 print("izquierda")
             elif evt.key == K_RIGHT:
                 print("derecha")  
             elif evt.key == K_UP:
                 print("arriba")  
             elif evt.key == K_DOWN:
                 print("abajo")  

    posX, posY = pygame.mouse.get_pos()
    posX = posX-100
    posY = posY-50

    pygame.display.update()