import pygame as pg

class Jugador(pg.sprite.Sprite):
	velocidad = 3
	ls_block = None
	ls_muros = None

	def __init__(self,imagen,a,b):
			pg.sprite.Sprite.__init__(self)
			self.m = imagen
			self.image=self.m[a][b]
			self.a = a
			self.b = b
			self.i = b
			self.dir = a
			self.rect=self.image.get_rect()
			self.rect.x=200
			self.rect.y=300
			self.hp = 50000
			self.band = 1
			self.band2 = 1

			self.staph = 0
			self.cd_staph = 80
			self.last_staph = pg.time.get_ticks()

			self.staph2 = 0
			self.cd_staph2 = 80
			self.last_staph2 = pg.time.get_ticks()

			self.cansado = 0
			self.cd_cansado = 5000
			self.last_cansado = pg.time.get_ticks()

	def move(self,dx,dy):
		if dx != 0:
			self.collide(dx, 0)
		if dy != 0:
			self.collide(0, dy)
		if self.staph == 0:
			self.staph = 1
			self.animate(dx, dy)

	def collide(self,dx,dy):
		self.rect.x += dx
		self.rect.y += dy

		ls_golpes=pg.sprite.spritecollide(self,self.ls_block,False)
		for g in ls_golpes:
			if dx>0:
				self.rect.right=g.rect.left
				dx = 0
			if dx<0:
				self.rect.left=g.rect.right
				dx = 0
			if dy>0:
				self.rect.bottom=g.rect.top
				dy = 0
			if dy<0:
				self.rect.top=g.rect.bottom
				dy = 0

		ls_colm=pg.sprite.spritecollide(self,self.ls_muros,False)
		for g in ls_colm:
			if dx>0:
				self.rect.right=g.rect.left
			if dx<0:
				self.rect.left=g.rect.right
			if dy>0:
				self.rect.bottom=g.rect.top
			if dy<0:
				self.rect.top=g.rect.bottom

	def animate(self, dx,dy):
		# Animacion
		if dx != 0 or dy != 0:
			if self.i < self.b + 2  and self.band == 1:
				self.i+=1
			else:
				self.i -= 1
				self.band=2
				if self.i==self.b:
					self.band=1
		else:
			self.i = 1
		self.image=self.m[self.i][self.dir]

	def ataque(self, a, b):
		if self.staph == 0:
			self.staph = 1
			if a < b + 2  and self.band2 == 1:
				a += 1
			else:
				a -= 1
				self.band2 = 2
				if a == b:
					self.band2=1

			self.image = self.m[a][self.dir]
