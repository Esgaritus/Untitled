import pygame as pg
import json as js
from Funciones import *


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

class Mapa3(object):
	def __init__(self, archivo):
		with open(archivo) as J_archivo:
			self.base = js.load(J_archivo)

		self.lsSombras4 = []
		self.lsSombras3 = []
		self.lsSombras = []
		self.lsOtros2 = []
		self.lsOtros = []
		self.lsDetail = []
		self.lsCosasC = []
		self.lsSombras2 = []
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
			if i['name'] == 'Otras cosas C':
				self.lsCosasC = i['data']
			if i['name'] == 'Otras cosas NC':
				self.lsCosasNC = i['data']
			if i['name'] == 'Ruinas Col':
				self.lsRuinas = i['data']
			if i['name'] == 'Suelo':
				self.lsSuelo = i['data']
			if i['name'] == 'Sombras 4':
				self.lsSombras4 = i['data']
			if i['name'] == 'Sombras 3':
				self.lsSombras3 = i['data']
			if i['name'] == 'Sombras 2':
				self.lsSombras2 = i['data']
			if i['name'] == 'Sombras':
				self.lsSombras = i['data']

		self.AnchoF = self.base['width']
		self.AltoF = self.base['height']
		self.lyOtros2 = self.Separar(self.lsOtros2, self.AnchoF)
		self.lyOtros = self.Separar(self.lsOtros, self.AnchoF)
		self.lyDetail = self.Separar(self.lsDetail, self.AnchoF)
		self.lyCosasC = self.Separar(self.lsCosasC, self.AnchoF)
		self.lyCosasNC = self.Separar(self.lsCosasNC, self.AnchoF)
		self.lyRuinas = self.Separar(self.lsRuinas, self.AnchoF)
		self.lySuelo = self.Separar(self.lsSuelo, self.AnchoF)
		self.lySombras4 = self.Separar(self.lsSombras4, self.AnchoF)
		self.lySombras3 = self.Separar(self.lsSombras3, self.AnchoF)
		self.lySombras2 = self.Separar(self.lsSombras2, self.AnchoF)
		self.lySombras = self.Separar(self.lsSombras, self.AnchoF)

		self.lstiles = self.Tiles()

	def Mapeo(self, Muros, Suelo, Detalles, OtsColisiones, Detalles2, Otros1, Otros2, Sombras4, Sombras3, Sombras2, Sombras):

		nf = 0
		for f in self.lyOtros2:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Otros2.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lyOtros:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Otros1.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lyDetail:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Detalles.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lyCosasC:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Colisionable(img, ne, nf)
					OtsColisiones.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lyCosasNC:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Detalles2.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lyRuinas:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Colisionable(img, ne, nf)
					Muros.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lySuelo:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Suelo.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lySombras4:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Sombras4.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lySombras3:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Sombras3.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lySombras2:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Sombras2.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lySombras:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Sombras.add(Col)
				ne += 32
			nf += 32

	def Tiles(self):
		l = []
		temp=[]
		for i in self.base['tilesets']:
			arc = i['image']
			lr = Recortar(arc, 32, 63)
			for t in lr:
				ltemp=[]
				for s in t:
					l.append(s)
					ltemp.append(s)
				temp.append(ltemp)
		result=[]
		for i in range(len(temp[0])):
			for j in temp:
				result.append(j[i])

		return result


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

class Mapa1(object):
	def __init__(self, archivo):
		with open(archivo) as J_archivo:
			self.base = js.load(J_archivo)

		self.lsDetallesNC = []
		self.lsObjetosC = []
		self.lsSombras3 = []
		self.lsSombras2 = []
		self.lsSombras1 = []
		self.lsBaseNC = []
		self.lsBaseC = []
		self.lsBaseNC2 = []
		self.lsBaseC2 = []

		for i in self.base['layers']:
			if i['name'] == 'Detalles NC':
				self.lsDetallesNC = i['data']
			if i['name'] == 'Objetos C':
				self.lsObjetosC = i['data']
			if i['name'] == 'Sombras 3':
				self.lsSombras3 = i['data']
			if i['name'] == 'Sombras 2':
				self.lsSombras2 = i['data']
			if i['name'] == 'Sombras 1':
				self.lsSombras1 = i['data']
			if i['name'] == 'Base NC':
				self.lsBaseNC = i['data']
			if i['name'] == 'Base C':
				self.lsBaseC = i['data']
			if i['name'] == 'Base NC2':
				self.lsBaseNC2 = i['data']
			if i['name'] == 'Base C2':
				self.lsBaseC2 = i['data']

		self.AnchoF = self.base['width']
		self.AltoF = self.base['height']
		self.lyDetallesNC = self.Separar(self.lsDetallesNC, self.AnchoF)
		self.lyObjetosC = self.Separar(self.lsObjetosC, self.AnchoF)
		self.lySombras3 = self.Separar(self.lsSombras3, self.AnchoF)
		self.lySombras2 = self.Separar(self.lsSombras2, self.AnchoF)
		self.lySombras1 = self.Separar(self.lsSombras1, self.AnchoF)
		self.lyBaseNC = self.Separar(self.lsBaseNC, self.AnchoF)
		self.lyBaseC = self.Separar(self.lsBaseC, self.AnchoF)
		self.lyBaseNC2 = self.Separar(self.lsBaseNC2, self.AnchoF)
		self.lyBaseC2 = self.Separar(self.lsBaseC2, self.AnchoF)

		self.lstiles = self.Tiles()

	def Mapeo(self, BaseC2, BaseNC2, BaseC, BaseNC, Sombras1, Sombras2, Sombras3, ObjetosC, DetallesNC):

		nf = 0
		for f in self.lyDetallesNC:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					DetallesNC.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lyObjetosC:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Colisionable(img, ne, nf)
					ObjetosC.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lySombras3:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Sombras3.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lySombras2:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Sombras2.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lySombras1:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					Sombras1.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lyBaseNC:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					BaseNC.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lyBaseC:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Colisionable(img, ne, nf)
					BaseC.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lyBaseNC2:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Otros(img, ne, nf)
					BaseNC2.add(Col)
				ne += 32
			nf += 32

		nf = 0
		for f in self.lyBaseC2:
			ne = 0
			for e in f:
				if e != 0:
					img = self.lstiles[e-1]
					Col = Colisionable(img, ne, nf)
					BaseC2.add(Col)
				ne += 32
			nf += 32



	def Tiles(self):
		l = []
		temp=[]
		for i in self.base['tilesets']:
			arc = i['image']
			lr = Recortar(arc, 32, 63)
			for t in lr:
				ltemp=[]
				for s in t:
					l.append(s)
					ltemp.append(s)
				temp.append(ltemp)
		result=[]
		for i in range(len(temp[0])):
			for j in temp:
				result.append(j[i])

		return result


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
