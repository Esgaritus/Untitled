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
	Rivales = pg.sprite.Group()

	# **************************************************************************
	# ______________________________ NIVELES ___________________________________

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
	Nivel1.Mapeo(BaseC2, BaseC, BaseNC, Sombras11, Sombras12, Sombras13, ObjetosC, DetallesNC)


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

	# **************************************************************************


	ImgPj1 = Recortar('Sprites/Pj1.png', 12, 8)
	# ImgPj2 = Recortar('Pj2.png', 12, 8)
	# ImgPj3 = Recortar('Pj3.png', 12, 8)
	ImgPollo1 = Recortar('Sprites/animales.png', 12, 8)
	ImgEspectro = Recortar('Sprites/Monster.png', 12, 8)
	ImgRhegal = Recortar('Sprites/Boss.png', 12, 8)

	Pj11 = Jugador(ImgPj1, 0, 0)
	Pj13 = Jugador(ImgPj1, 0, 0)
	# Pj2 = Jugador(ImgPj2, 0, 0)
	# Pj3 = Jugador(ImgPj3, 0, 0)

	Pj11.ls_block = ObjetosC
	Pj11.ls_muros = BaseC

	Pollo1 = Boss(ImgPollo1, 3, 4)
	Pollo1.ls_muros = Muros
	Pollo1.ls_block = OtsColisiones

	Espectro = Boss(ImgEspectro, 3, 4)

	Rhegal = Boss(ImgRhegal, 0, 0)
	Rhegal.ls_muros = Muros
	Rhegal.ls_block = OtsColisiones
	Rhegal.ls_proy = Proyectiles


	Personajes = pg.sprite.Group()
	Personajes.add(Pj11)
	# Personajes.add(Pj2)
	# Personajes.add(Pj3)

	camara1 = Camara(Pantalla, Pj11.rect,Nivel1.AnchoF*32,Nivel3.AltoF*32)
	camara3 = Camara(Pantalla, Pj11.rect,Nivel3.AnchoF*32,Nivel3.AltoF*32)


	Running = True
	while Running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				Running = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					Running = False


		now = pg.time.get_ticks()
		if now - Pj11.last_staph >= Pj11.cd_staph:
			Pj11.staph = 0
			Pj11.last_staph = now

		if now - Pj11.last_cansado >= Pj11.cd_cansado:
			Pj11.cansado = 0
			Pj11.last_cansado = now

		key = pg.key.get_pressed()

		if key[pg.K_a]:
			Pj11.move(-Pj11.velocidad, 0)
			Pj11.dir = 1

		if key[pg.K_d]:
			Pj11.move(Pj11.velocidad, 0)
			Pj11.dir = 2

		if key[pg.K_w]:
			Pj11.move(0, -Pj11.velocidad)
			Pj11.dir = 3

		if key[pg.K_s]:
			Pj11.move(0, Pj11.velocidad)
			Pj11.dir = 0

		now2 = pg.time.get_ticks()
		if key[pg.K_SPACE]:
			if Pj11.cansado <= 0:
				Pj11.cansado = 1000
			else:
				Pj11.cansado -= 1
			Pj11.velocidad = 5
		else:
			Pj11.velocidad = 3


		Personajes.update()

		pg.display.flip()

		Pantalla.fill((0,0,0))
		camara1.actualizar()
		camara1.dibujarSprites(Pantalla, BaseC2)
		camara1.dibujarSprites(Pantalla, BaseNC2)
		camara1.dibujarSprites(Pantalla, BaseC)
		camara1.dibujarSprites(Pantalla, BaseNC)
		camara1.dibujarSprites(Pantalla, Sombras11)
		camara1.dibujarSprites(Pantalla, Sombras12)
		camara1.dibujarSprites(Pantalla, Personajes)
		camara1.dibujarSprites(Pantalla, DetallesNC)
		camara1.dibujarSprites(Pantalla, Sombras13)
		camara1.dibujarSprites(Pantalla, ObjetosC)


		# camara3.actualizar()
		# camara3.dibujarSprites(Pantalla, Suelo)
		# camara3.dibujarSprites(Pantalla, Muros)
		# camara3.dibujarSprites(Pantalla, Detalles2)
		# camara3.dibujarSprites(Pantalla, Personajes)
		# camara3.dibujarSprites(Pantalla, OtsColisiones)
		# camara3.dibujarSprites(Pantalla, Sombras32)
		# camara3.dibujarSprites(Pantalla, Detalles)
		# camara3.dibujarSprites(Pantalla, Otros1)
		# camara3.dibujarSprites(Pantalla, Otros2)
		# camara3.dibujarSprites(Pantalla, Sombras34)
		# camara3.dibujarSprites(Pantalla, Sombras33)
		# camara3.dibujarSprites(Pantalla, Sombras31)


		Reloj.tick(60)
		pg.display.flip()
