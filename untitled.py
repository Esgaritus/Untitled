import pygame as pg
import json as js

n = 32
m = 26

Ancho = n*32
Alto = m*32

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

    def Mapeo(self, Colisionables, NoColisionables):
        nf = 0
        for f in self.lyOtros2:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e]
                    Col = Otros(img, nf, ne)
                    NoColisionables.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lyOtros:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Otros(img, nf, ne)
                    NoColisionables.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lyDetail:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Otros(img, nf, ne)
                    NoColisionables.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lyCosasC:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Colisionables(img, nf, ne)
                    Colisionables.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lyCosasNC:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Otros(img, nf, ne)
                    NoColisionables.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lyRuinas:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Colisionable(img, nf, ne)
                    Colisionables.add(Col)
                ne += 32
            nf += 32

        nf = 0
        for f in self.lySuelo:
            ne = 0
            for e in f:
                if e != 0:
                    img = self.lstiles[e-1]
                    Col = Otros(img, nf, ne)
                    NoColisionables.add(Col)
                ne += 32
            nf += 32


    def Tiles(self):
        l = []
        for i in self.base['tilesets']:
            arc = i['image']
            lr = Recortar(arc, 32, 64)
            for t in lr:
                l.append(t)
        return l


    def Separar(self, lista, ancho):
        cont = 0
        m = []
        linea = []
        for i in lista:
            linea.append(i)
            cont+=1
            if cont == ancho:
                m.append(linea)
                linea = []
                cont = 0
        return m


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


if __name__ == '__main__':
    pg. init()
    Pantalla = pg.display.set_mode([Ancho, Alto])

    Colisionables = pg.sprite.Group()
    NoColisionables = pg.sprite.Group()

    Nivel = Mapa('untitledmap.json')
    Nivel.Mapeo(Colisionables, NoColisionables)

    Running = True
    while Running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    Running = False

        Colisionables.draw(Pantalla)
        NoColisionables.draw(Pantalla)
