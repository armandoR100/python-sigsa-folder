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
        #print("rectangulo : "+str(self.rect))

    def movimientoDerecha(self):
        self.rect.right += self.Velocidad
        self.__movimiento()
    
    def movimientoIzquierda(self):
        self.rect.left -= self.Velocidad
        self.__movimiento()

    def __movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0 :
                self.rect.left = 0
            elif self.rect.right > 870 :
                self.rect.right = 840

    def disparar(self, x ,y):
        miProyectil = Proyectil(x,y, directorio+"disparoa.jpg", True)
        self.listaDisparo.append(miProyectil)        
        print("disparo_a")

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)
#-----------------------------------------------

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenProyectil = pygame.image.load(ruta)
        self.rect = self.ImagenProyectil.get_rect()
        self.VelocidadDisparo = 5
        self.rect.top = posy
        self.rect.left = posx
        self.disparoPersonaje = personaje
    
    def trayectoria(self):
        if self.disparoPersonaje == True:
            self.rect.top = self.rect.top - self.VelocidadDisparo
        else:
            self.rect.top = self.rect.top + self.VelocidadDisparo

    def dibujar(self, superficie):
        superficie.blit(self.ImagenProyectil, self.rect)    
#-----------------------------------------------

class Invasor(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenA = pygame.image.load(directorio+"MarcianoA.jpg")
        self.ImagenB = pygame.image.load(directorio+"MarcianoB.jpg")
        self.listaImagenes = [self.ImagenA, self.ImagenB]
        self.posImagen = 0
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        self.rect = self.imagenInvasor.get_rect()
        self.ListaDisparo = []
        self.VelocidadDisparo = 20
        self.rect.top = posy
        self.rect.left = posx
        
        self.rangoDisparo = 5
        self.tiempoCambio = 1
        
        self.derecha = True
        self.contador = 0 
        self.MaxDescenso = self.rect.top+40
        
    def dibujar(self, superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)
 
    def comportamiento(self, tiempo):
        self.__movimientos()
        self.__ataque()
        
        if self.tiempoCambio == tiempo:
            self.posImagen +=1
            self.tiempoCambio +=1
            if self.posImagen > len(self.listaImagenes)-1:
                self.posImagen = 0
    
    def __movimientos(self):
        if self.contador<3:
            self.__movimientoLateral()
        else:
            self.__descenso()
    
    def __descenso(self):
        if self.MaxDescenso == self.rect.top:
            self.contador = 0
            self.MaxDescenso = self.rect.top+40
        else:
            self.rect.top +=1
        
    
    def __movimientoLateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left + self.VelocidadDisparo
            if self.rect.left > 500:
                self.derecha = False
                self.contador +=1
        else:
            self.rect.left = self.rect.left - self.VelocidadDisparo
            if self.rect.left < 0:
                self.derecha = True
    
    def __ataque(self):
        if (randint(0,100) < self.rangoDisparo):
            self.__disparo()
        
    def __disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil(x,y,directorio+"disparob.jpg", False)
        self.ListaDisparo.append(miProyectil)
        print("disparo_b")        
#------------------------------------------------
def SpaceInvander():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Hola mundo")
    ImagenFondo = pygame.image.load(directorio+"Fondo.jpg")
    
    jugador = naveEspacial()
    enemigo = Invasor(100,100)
    enJuego = True
    reloj = pygame.time.Clock()

    while True:  
        reloj.tick(60)
        tiempo = int(pygame.time.get_ticks()/1000)
         
        for evt in pygame.event.get():
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
            if enJuego == True:
                if evt.type == pygame.KEYDOWN:
                    if evt.key == K_LEFT:
                        jugador.movimientoIzquierda()                
                    elif evt.key == K_RIGHT:
                        jugador.movimientoDerecha()
                    elif evt.key == K_s:
                        x, y = jugador.rect.center
                        jugador.disparar(x , y) 

        ventana.blit(ImagenFondo, (0,0) )
        enemigo.comportamiento(tiempo)
        jugador.dibujar(ventana)
        enemigo.dibujar(ventana)
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top <-10:
                    jugador.listaDisparo.remove(x)
        
        if len(enemigo.ListaDisparo) > 0:
            for x in enemigo.ListaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                
                if x.rect.top > 900:
                    enemigo.ListaDisparo.remove(x)

        pygame.display.update() 

SpaceInvander()