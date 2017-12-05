import pygame as pg
from pygame.locals import *

def Recortar(archivo, an,al):
	fondo = pg.image.load(archivo).convert_alpha()
	info = fondo.get_size()
	img_ancho = info[0]
	img_alto = info[1]
	corte_x = img_ancho/an
	corte_y = img_alto/al

	m=[]
	for i in range(an):
		fila=[]
		for j in range(al):
			cuadro = [i*corte_x, j*corte_y, corte_x, corte_y]
			recorte = fondo.subsurface(cuadro)
			fila.append(recorte)
		m.append(fila)

	return m

def RelRect(actor, camara):
	return pg.Rect(actor.rect.x-camara.rect.x, actor.rect.y-camara.rect.y, actor.rect.w, actor.rect.h)

class Camara(object): #clase camara

	def __init__(self, pantalla, jugador, anchoNivel, largoNivel):
		self.jugador = jugador
		self.rect = pantalla.get_rect()
		self.rect.center = self.jugador.center
		self.mundo_rect = Rect(0, 0, anchoNivel, largoNivel)

	def actualizar(self):
	  if self.jugador.centerx > self.rect.centerx + 25:
		  self.rect.centerx = self.jugador.centerx - 25

	  if self.jugador.centerx < self.rect.centerx - 25:
		  self.rect.centerx = self.jugador.centerx + 25

	  if self.jugador.centery > self.rect.centery + 25:
		  self.rect.centery = self.jugador.centery - 25

	  if self.jugador.centery < self.rect.centery - 25:
		  self.rect.centery = self.jugador.centery + 25
	  self.rect.clamp_ip(self.mundo_rect)

	def dibujarSprites(self, pantalla, sprites):
		for s in sprites:
			if s.rect.colliderect(self.rect):
				pantalla.blit(s.image, RelRect(s, self))
