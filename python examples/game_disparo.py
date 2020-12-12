import pygame,sys 
from pygame.locals import *
from random  import randint

#VARIABLES GLOBALES
ancho = 900
alto = 400
directorio = "C:/Users/JorgeRomero/Desktop/imagenes/"

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load(directorio+"nave.jpg")

        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-30
        self.listaDisparo = []
        self.Vida = True
        self.Velocidad = 20
        print(self.rect)

    def movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0 :
                self.rect.left = 0
            elif self.rect.right > 870 :
                self.rect.right = 840

    def disparar(self, x ,y):
        miProyectil = Proyectil(x,y)
        self.listaDisparo.append(miProyectil)        
        print("disparo")

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)
#-----------------------------------------------

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenProyectil = pygame.image.load(directorio+"disparoa.jpg")
        self.rect = self.ImagenProyectil.get_rect()
        self.VelocidadDisparo = 5
        self.rect.top = posy
        self.rect.left = posx
    
    def trayectoria(self):
        self.rect.top = self.rect.top - self.VelocidadDisparo

    def dibujar(self, superficie):
        superficie.blit(self.ImagenProyectil, self.rect)    

#------------------------------------------------
def SpaceInvander():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Hola mundo")
    ImagenFondo = pygame.image.load(directorio+"Fondo2.jpg")

    jugador = naveEspacial()
    DemoProyectil = Proyectil(ancho/2, alto-30)
    enJuego = True

    while True:  

        jugador.movimiento()
        DemoProyectil.trayectoria()
        for evt in pygame.event.get():
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if enJuego == True:
                if evt.type == pygame.KEYDOWN:
                    if evt.key == K_LEFT:
                        jugador.rect.left -= jugador.Velocidad
                    
                    elif evt.key == K_RIGHT:
                        jugador.rect.right += jugador.Velocidad
                    elif evt.key == K_s:
                        x, y = jugador.rect.center
                        jugador.disparar(x , y) 

        ventana.blit(ImagenFondo, (0,0) )
        #DemoProyectil.dibujar(ventana)//dispara una sola vez
        jugador.dibujar(ventana)

        if len(jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top < 200:
                    jugador.listaDisparo.remove(x)

        pygame.display.update() 

SpaceInvander()