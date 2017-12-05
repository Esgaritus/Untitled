import pygame as pg
import random
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
	Luz = pg.image.load('Mapas/light.png').convert_alpha()
	Light = Otros(Luz, 8*32, 0)

	Efectos = pg.sprite.Group()
	Proyectiles = pg.sprite.Group()
	Rivales = pg.sprite.Group()
	Eventos = pg.sprite.Group()
	Eventos2 = pg.sprite.Group()

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
	Espant = pg.sprite.Group()

	Nivel1 = Mapa1('Mapas/Mapa1.json')
	Nivel1.Mapeo(BaseC2, BaseC, BaseNC, Sombras11, Sombras12, Sombras13, ObjetosC, DetallesNC, Espant)

	#Nivel 2
	Colisiona = pg.sprite.Group()
	Fondo = pg.sprite.Group()
	Rivales2 = pg.sprite.Group()

	Nivel2 = Mapa2('Mapas/Mapa2.json')
	Nivel2.Mapeo(Colisiona, Fondo)


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

	Nivel3 = Mapa3('Mapas/Mapa3.json')
	Nivel3.Mapeo(Muros, Suelo, Detalles, OtsColisiones, Detalles2, Otros1, Otros2, Sombras34, Sombras33, Sombras32, Sombras31)

	# **************************************************************************


	ImgPj1 = Recortar('Sprites/muneco.png', 12, 8)
	# ImgPj2 = Recortar('Pj2.png', 12, 8)
	# ImgPj3 = Recortar('Pj3.png', 12, 8)
	ImgPollo1 = Recortar('Sprites/animales.png', 12, 8)
	ImgEspectro = Recortar('Sprites/Monster.png', 12, 8)
	ImgRhegal = Recortar('Sprites/Boss.png', 12, 8)



	Pj11 = Jugador(ImgPj1, 0, 0)
	Pj12 = Jugador(ImgPj1, 0, 0)
	Pj13 = Jugador(ImgPj1, 0, 0)
	# Pj2 = Jugador(ImgPj2, 0, 0)
	# Pj3 = Jugador(ImgPj3, 0, 0)

	Pj = Pj11

	Pj11.ls_block = ObjetosC
	Pj11.ls_muros = BaseC

	Pj12.ls_block = Colisiona
	Pj12.ls_muros = Colisiona

	Pj12.rect.x = 500
	Pj12.rect.x = 600

	Pj13.ls_block = OtsColisiones
	Pj13.ls_muros = Muros


	for i in range(4):
		Pollo1 = Boss(ImgPollo1, 3, 4)
		posrandx = random.randint(0, 1500)
		posrandy = random.randint(0, 1000)
		Pollo1.rect.x = posrandx
		Pollo1.rect.y = posrandy
		Pollo1.jp = Pj12
		Pollo1.ls_proy = Proyectiles
		Pollo1.ls_muros = Eventos2
		Pollo1.ls_block = Colisiona
		Rivales2.add(Pollo1)

	Espectro = Boss(ImgEspectro, 3, 4)

	Rhegal = Boss(ImgRhegal, 0, 0)
	Rhegal.ls_muros = Muros
	Rhegal.ls_block = OtsColisiones
	Rhegal.ls_proy = Proyectiles


	Personajes1 = pg.sprite.Group()
	Personajes2 = pg.sprite.Group()
	Personajes3 = pg.sprite.Group()

	Personajes1.add(Pj11)
	Personajes2.add(Pj12)
	Personajes3.add(Pj13)
	# Personajes.add(Pj2)
	# Personajes.add(Pj3)

	# Eventos
	dragon = Dragon(20, 16, 2 , 1)
	espantapajaros = Dragon(15, 14, 1, 1)
	Eventos.add(dragon)
	Eventos.add(espantapajaros)

	pasar = Dragon(74, 19, 1, 2)
	Eventos2.add(pasar)


	camara1 = Camara(Pantalla, Pj11.rect, Nivel1.AnchoF*32,Nivel1.AltoF*32)
	camara2 = Camara(Pantalla, Pj12.rect, Nivel2.AnchoF*32,Nivel2.AltoF*32)
	camara3 = Camara(Pantalla, Pj13.rect, Nivel3.AnchoF*32,Nivel3.AltoF*32)

	Band_lv1 = True
	Band_lv2 = False
	Band_lv3 = False

	bandera = False

	banderaK = True
	last_banderaK = pg.time.get_ticks()
	cd = 120

	objeto1 = 1
	estado = 0
	objeto2 = 0
	estado2 = 0

	Pause = False
	Running = True

	while Running:

		for event in pg.event.get():
			if event.type == pg.QUIT:
				Running = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					Running = False

		now = pg.time.get_ticks()

		if now - Pj.last_staph >= Pj.cd_staph:
			Pj.staph = 0
			Pj.last_staph = now

		if now - Pj.last_staph2 >= Pj.cd_staph2:
			Pj.staph2 = 0
			Pj.last_staph2 = now

		if now - Pj.last_cansado >= Pj.cd_cansado:
			Pj.cansado = 0
			Pj.last_cansado = now

		if now - last_banderaK >= cd:
			banderaK = True
			last_banderaK = now

		key = pg.key.get_pressed()

		if key[pg.K_a]:
			Pj.move(-Pj.velocidad, 0)
			Pj.dir = 1

		if key[pg.K_d]:
			Pj.move(Pj.velocidad, 0)
			Pj.dir = 2

		if key[pg.K_w]:
			Pj.move(0, -Pj.velocidad)
			Pj.dir = 3

		if key[pg.K_s]:
			Pj.move(0, Pj.velocidad)
			Pj.dir = 0

		if banderaK:
			if key[pg.K_k]:
				Pj.ataque(6,6)
				banderaK = False
				bandera = True

			else:
				bandera = False

		Pj.move(0,0)


		if(pg.sprite.collide_rect(Pj11, espantapajaros)):
			if(bandera):
				print ("Espantapajaros Golpeado ", espantapajaros.vida)
				espantapajaros.vida -= 10
				bandera = False
				if espantapajaros.vida <= 0:
					objeto1 = 0
					Espant.empty()
					Eventos.remove(espantapajaros)




		now2 = pg.time.get_ticks()
		if key[pg.K_SPACE]:
			if Pj11.cansado <= 0:
				Pj11.cansado = 1000
			else:
				Pj11.cansado -= 1
			Pj11.velocidad = 5
		else:
			Pj11.velocidad = 3

		if(pg.sprite.collide_rect(Pj11, dragon)):
			if(objeto1==0):
				estado = 1

			else:
				if Pj11.rect.x > 0:
					Pj11.rect.right = dragon.rect.left
				else:
					Pj11.rect.left = dragon.rect.right

		if(pg.sprite.collide_rect(Pj12, pasar)):
			if( objeto2 == 0):
				estado2 = 1
			else:
				if Pj11.rect.x > 0:
					Pj11.rect.right = dragon.rect.left
				else:
					Pj11.rect.left = dragon.rect.right

		if estado == 1:
			Band_lv1 = False
			Band_lv2 = True
			Personajes1.empty()
			BaseC2.empty()
			BaseNC2.empty()
			BaseC.empty()
			BaseNC.empty()
			Sombras11.empty()
			Sombras12.empty()
			DetallesNC.empty()
			Sombras13.empty()
			ObjetosC.empty()
			Eventos.empty()
			Espant.empty()

		if estado2 == 1:
			Band_lv2 = False
			Band_lv3 = True
			Colisiona.empty()
			Fondo.empty()
			Personajes2.empty()
			Eventos2.empty()


		pg.display.flip()
		if Band_lv1:
			Pj = Pj11
			Personajes1.update()
			Pantalla.fill((0,0,0))
			camara1.actualizar()
			camara1.dibujarSprites(Pantalla, Eventos)
			camara1.dibujarSprites(Pantalla, BaseC2)
			camara1.dibujarSprites(Pantalla, BaseNC2)
			camara1.dibujarSprites(Pantalla, BaseC)
			camara1.dibujarSprites(Pantalla, BaseNC)
			camara1.dibujarSprites(Pantalla, Sombras11)
			camara1.dibujarSprites(Pantalla, Sombras12)
			camara1.dibujarSprites(Pantalla, Personajes1)
			camara1.dibujarSprites(Pantalla, DetallesNC)
			camara1.dibujarSprites(Pantalla, Sombras13)
			camara1.dibujarSprites(Pantalla, ObjetosC)
			camara1.dibujarSprites(Pantalla, Espant)

		elif Band_lv2:
			Pj = Pj12
			Pantalla.fill((0,0,0))
			Rivales2.update()
			camara2.actualizar()
			camara2.dibujarSprites(Pantalla, Colisiona)
			camara2.dibujarSprites(Pantalla, Fondo)
			camara2.dibujarSprites(Pantalla, Personajes2)
			camara2.dibujarSprites(Pantalla, Rivales2)
			camara2.dibujarSprites(Pantalla, Eventos2)

		elif Band_lv3:
			Pj = Pj13
			camara3.actualizar()
			camara3.dibujarSprites(Pantalla, Suelo)
			camara3.dibujarSprites(Pantalla, Muros)
			camara3.dibujarSprites(Pantalla, Detalles2)
			camara3.dibujarSprites(Pantalla, Personajes3)
			camara3.dibujarSprites(Pantalla, OtsColisiones)
			camara3.dibujarSprites(Pantalla, Sombras32)
			camara3.dibujarSprites(Pantalla, Detalles)
			camara3.dibujarSprites(Pantalla, Otros1)
			camara3.dibujarSprites(Pantalla, Otros2)
			camara3.dibujarSprites(Pantalla, Sombras34)
			camara3.dibujarSprites(Pantalla, Sombras33)
			camara3.dibujarSprites(Pantalla, Sombras31)

		Reloj.tick(60)
		pg.display.flip()
