import pygame as pg

def gestionar_ventana():
    pg.init()

    ancho = 800
    alto = 800
    ventana = pg.display.set_mode((ancho,alto))

    pg.display.set_caption("Juego de prueba")

    run = True 
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
    pg.quit()
    return run 

def gestionar_personaje(): 
    class Personaje():
        def __init__(self,x,y):
            self.forma = pg.Rect(0,0,20,20)
            self.forma.center = (x,y)
        def dibujar(self,interfaz):
            pg.draw.rect(interfaz,(255,255,255),self.forma)
    jugador = Personaje(400,400)

gestionar_ventana()