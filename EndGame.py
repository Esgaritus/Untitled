import pygame as pg
import json as js
from Clases import *
from Personajes import *
from Funciones import *
from BossAgent import *

n = 32
m = 26

Ancho = 800
Alto = 600


if __name__ == '__main__':
	pg. init()
	Pantalla = pg.display.set_mode([Ancho, Alto])
	Reloj = pg.time.Clock()
	Luz = pg.image.load('light.png').convert_alpha()
	Light = Otros(Luz, 8*32, 0)

	Efectos = pg.sprite.Group()
	Proyectiles = pg.sprite.Group()

	# Nivel 1
	BaseC2 = pg.sprite.Group()
	BaseNC2 = pg.sprite.Group()
	BaseC = pg.sprite.Group()
	BaseNC = pg.sprite.Group()
	Sombras11 = pg.sprite.Group()
	Sombras12 = pg.sprite.Group()
	Sombras13 = pg.sprite.Group()
	ObjetosC = pg.sprite.Group()
	DetallesNC = pg.sprite.Group()

	Nivel1 = Mapa1('Mapa1.json')
	Nivel1.Mapeo(BaseC2, BaseNC2, BaseC, BaseNC, Sombras11, Sombras12, Sombras13, ObjetosC, DetallesNC)

	# Nivel 3
	Muros = pg.sprite.Group()
	Suelo = pg.sprite.Group()
	Detalles = pg.sprite.Group()
	Detalles2= pg.sprite.Group()
	OtsColisiones = pg.sprite.Group()
	Otros1 = pg.sprite.Group()
	Otros2 = pg.sprite.Group()
	Sombras34 = pg.sprite.Group()
	Sombras33 = pg.sprite.Group()
	Sombras32 = pg.sprite.Group()
	Sombras31 = pg.sprite.Group()

	Nivel3 = Mapa3('Mapa3.json')
	Nivel3.Mapeo(Muros, Suelo, Detalles, OtsColisiones, Detalles2, Otros1, Otros2, Sombras34, Sombras33, Sombras32, Sombras31)


	ImgPj1 = Recortar('Pj1.png', 12, 8)
	# ImgPj2 = Recortar('Pj2.png', 12, 8)
	# ImgPj3 = Recortar('Pj3.png', 12, 8)

	Pj1 = Jugador(ImgPj1, 0, 0)
	# Pj2 = Jugador(ImgPj2, 0, 0)
	# Pj3 = Jugador(ImgPj3, 0, 0)

	Pj1.ls_block = OtsColisiones
	Pj1.ls_muros = Muros

	Rhegal = Boss('Boss.png', 0, 0)
	Rhegal.ls_muros = Muros
	Rhegal.ls_block = OtsColisiones
	Rhegal.ls_proy = Proyectiles


	Personajes = pg.sprite.Group()
	Personajes.add(Pj1)
	# Personajes.add(Pj2)
	# Personajes.add(Pj3)

	camara = Camara(Pantalla, Pj1.rect,Nivel3.AnchoF*32,Nivel3.AltoF*32)

	Running = True
	while Running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				Running = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					Running = False


		now = pg.time.get_ticks()
		if now - Pj1.last_staph >= Pj1.cd_staph:
			Pj1.staph = 0
			Pj1.last_staph = now

		if now - Pj1.last_cansado >= Pj1.cd_cansado:
			Pj1.cansado = 0
			Pj1.last_cansado = now

		key = pg.key.get_pressed()

		if key[pg.K_a]:
			Pj1.move(-Pj1.velocidad, 0)
			Pj1.dir = 1

		if key[pg.K_d]:
			Pj1.move(Pj1.velocidad, 0)
			Pj1.dir = 2

		if key[pg.K_w]:
			Pj1.move(0, -Pj1.velocidad)
			Pj1.dir = 3

		if key[pg.K_s]:
			Pj1.move(0, Pj1.velocidad)
			Pj1.dir = 0

		now2 = pg.time.get_ticks()
		if key[pg.K_SPACE]:
			if Pj1.cansado <= 0:
				Pj1.cansado = 1000
			else:
				Pj1.cansado -= 1
			Pj1.velocidad = 5
		else:
			Pj1.velocidad = 3


		Personajes.update()

		pg.display.flip()
		camara.actualizar()
		camara.dibujarSprites(Pantalla, Suelo)
		camara.dibujarSprites(Pantalla, Muros)
		camara.dibujarSprites(Pantalla, Detalles2)
		camara.dibujarSprites(Pantalla, Personajes)
		camara.dibujarSprites(Pantalla, OtsColisiones)
		camara.dibujarSprites(Pantalla, Sombras32)
		camara.dibujarSprites(Pantalla, Detalles)
		camara.dibujarSprites(Pantalla, Otros1)
		camara.dibujarSprites(Pantalla, Otros2)
		camara.dibujarSprites(Pantalla, Sombras34)
		camara.dibujarSprites(Pantalla, Sombras33)
		camara.dibujarSprites(Pantalla, Sombras31)


		Reloj.tick(60)
		pg.display.flip()
