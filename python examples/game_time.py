import pygame,sys 
from pygame.locals import *
from random  import randint

pygame.init()
ventana = pygame.display.set_mode((600,300))
pygame.display.set_caption("Hola mundo")
fuente = pygame.font.SysFont("Arial",30)

aux=1
while True:  
    ventana.fill((255,255,255))
    Tiempo = pygame.time.get_ticks()/1000

    if aux== Tiempo:
        aux+=1
        print(Tiempo)

    for evt in pygame.event.get():
        if evt.type == QUIT:
            pygame.quit()
            sys.exit()
    
    contador = fuente.render("Tiempo : "+str(Tiempo),0,(120,70,0))
    ventana.blit(contador,(100,100))
    pygame.display.update()