import pygame as pg
import json as js
from pygame.locals import *
from BossAgent import *

n = 32 #32
m = 26 #26

Ancho = n*32
Alto = m*32


IZQUIERDA=0
DERECHA=1
ABAJO=2
ARRIBA=3

NEGRO=(0,0,0)


class Colisionable(pg.sprite.Sprite):
    def __init__(self, img, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Otros(pg.sprite.Sprite):
    def __init__(self, img, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class jugador(pg.sprite.Sprite):
	velocidad=4
	ls_block=None

	def __init__(self,imagen,a,b):
			pg.sprite.Sprite.__init__(self)
			self.m = imagen
			self.image=self.m[a][b]
			self.a = a
			self.b = b
			self.i = b
			self.dir = a
			self.rect=self.image.get_rect()
			self.rect.x=100
			self.rect.y=100
			self.hp = 50000
			self.band = 1

	def move(self,dx,dy):
		if dx != 0:
			self.collide(dx, 0)
		if dy != 0:
			self.collide(0, dy)
		self.animate(dx, dy)

	def collide(self,dx,dy):
		self.rect.x += dx
		self.rect.y += dy

		# ls_golpes=pg.sprite.spritecollide(self,self.ls_block,False)
		# for g in ls_golpes:
		# 	if dx>0:
		# 		self.rect.right=g.rect.left
		# 	if dx<0:
		# 		self.rect.left=g.rect.right
		# 	if dy>0:
		# 		self.rect.bottom=g.rect.top
		# 	if dy<0:
		# 		self.rect.top=g.rect.bottom

	def animate(self, dx,dy):
		# Animacion
		if dx != 0 or dy != 0:
			if self.i < self.b + 2  and self.band == 1:
				self.i+=1
			else:
				self.i -= 1
				self.band=2
				if self.i==0:
					self.band=1
		else:
			self.i = 1
		self.image=self.m[self.i][self.dir]

class Mapa(object):
    def __init__(self, archivo):
        with open(archivo) as J_archivo:
            self.base = js.load(J_archivo)

        self.lsOtros2 = []
        self.lsOtros = []
        self.lsDetail = []
        self.lsCosasC = []
        self.lsCosasNC = []
        self.lsRuinas = []
        self.lsSuelo = []

        for i in self.base['layers']:
            if i['name'] == 'Otros 2':
                self.lsOtros2 = i['data']
            if i['name'] == 'Otros':
                self.lsOtros = i['data']
            if i['name'] == 'Detalles (encima)':
                self.lsDetail = i['data']
            if i['name'] == 'Otras Cosas C':
                self.lsCosasC = i['data']
            if i['name'] == 'Otras Cosas NC':
                self.lsCosasNC = i['data']
            if i['name'] == 'Ruinas Col':
                self.lsRuinas = i['data']
            if i['name'] == 'Suelo':
                self.lsSuelo = i['data']

        self.AnchoF = self.base['width']
        self.AltoF = self.base['height']
        self.lyOtros2 = self.Separar(self.lsOtros2, self.AnchoF)
        self.lyOtros = self.Separar(self.lsOtros, self.AnchoF)
        self.lyDetail = self.Separar(self.lsDetail, self.AnchoF)
        self.lyCosasC = self.Separar(self.lsCosasC, self.AnchoF)
        self.lyCosasNC = self.Separar(self.lsCosasNC, self.AnchoF)
        self.lyRuinas = self.Separar(self.lsRuinas, self.AnchoF)
        self.lySuelo = self.Separar(self.lsSuelo, self.AnchoF)

        self.lstiles = self.Tiles()

    def Mapeo(self, Colisionables, NoColisionables, Bloques):
        nf = 0
        for f in self.lyOtros2:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]

                    Col = Otros(img, ne, nf)
                    NoColisionables.add(Col)
                    #pantalla.blit(img,[110,110])
                ne += 32
            nf += 32

        nf = 0
        for f in self.lyOtros:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Otros(img, ne, nf)
                    NoColisionables.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lyDetail:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Otros(img, ne, nf)
                    NoColisionables.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lyCosasC:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Colisionables(img, ne, nf)
                    Bloques.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lyCosasNC:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Otros(img, ne, nf)
                    NoColisionables.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lyRuinas:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Colisionable(img, ne, nf)
                    Bloques.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lySuelo:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Otros(img, ne, nf)
                    NoColisionables.add(Col)
                ne += 32
            nf += 32


    def Tiles(self):
        l = []
        for i in self.base['tilesets']:
            arc = i['image']
            lr = self.Recortar(arc, 32, 32)
            for t in lr:
                l.append(t)
        return l


    def Separar(self,l, ancho):
        con=0
        matriz=[]
        linea=[]
        for i in l:
            linea.append(i)
            con+=1
            if con==ancho:
                matriz.append(linea)
                linea=[]
                con=0
        return matriz

    def Recortar(self,archivo, anc, alc):
        linea=[]
        imagen=pg.image.load(archivo).convert_alpha()
        i_ancho, i_alto=imagen.get_size()
        for y in range(0, i_alto/alc):
            for x in range(0,i_ancho/anc):
                cuadro=(x*anc, y*alc, anc, alc)
                linea.append(imagen.subsurface(cuadro))
        return linea

def Recortar(archivo, an,al):
	fondo = pg.image.load(archivo).convert_alpha()
	info=fondo.get_size()
	img_ancho=info[0]
	img_alto=info[1]
	corte_x=img_ancho/an
	corte_y=img_alto/al

	m=[]
	for i in range(an):
		fila=[]
		for j in range(al):
			cuadro=[i*corte_x,j*corte_y,corte_x,corte_y]
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


if __name__ == '__main__':
    pg. init()
    pantalla = pg.display.set_mode([Ancho, Alto])

    Colisionables = pg.sprite.Group()
    NoColisionables = pg.sprite.Group()
    Bloques = pg.sprite.Group()
    proyectiles = pg.sprite.Group()

    todos = pg.sprite.Group()

    Nivel = Mapa('untitledmap.json')
    Nivel.Mapeo(Colisionables, NoColisionables, Bloques)

    Imgjp = Recortar("Pj1.png",12,8)
    jp= jugador(Imgjp, 0, 0)
    jp.ls_block=Colisionables

    ImgBoss = Recortar('Boss.png', 12, 8)

    boss = Boss(ImgBoss, 0, 0)
    boss.jp = jp
    boss.ls_muros = Colisionables
    boss.ls_block = Bloques
    boss.ls_proy = proyectiles

    todos.add(boss)

    camara = Camara(pantalla, jp.rect,Nivel.AnchoF*32,Nivel.AltoF*32)
    todos.add(jp)
    reloj=pg.time.Clock()
    Running = True
    while Running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    Running = False
        key = pg.key.get_pressed()

        if key[pg.K_a]:
            jp.facing=IZQUIERDA
            jp.move(-jp.velocidad, 0)

        if key[pg.K_d]:
            jp.move(jp.velocidad, 0)
            jp.facing=DERECHA

        if key[pg.K_w]:
            jp.move(0, -jp.velocidad)
            jp.facing=ARRIBA

        if key[pg.K_s]:
            jp.move(0, jp.velocidad)
            jp.facing=ABAJO

        boss.update()
        proyectiles.update()
        pantalla.fill(NEGRO)
        camara.actualizar()
        camara.dibujarSprites(pantalla, NoColisionables)
        camara.dibujarSprites(pantalla, Bloques)
        camara.dibujarSprites(pantalla, todos)
        camara.dibujarSprites(pantalla, proyectiles)
        pg.display.flip()
        reloj.tick(60)
