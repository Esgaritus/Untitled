import random
import pygame as pg

def SimpleReflexAtackingBoss(bossSprt, table):
	pass

def get_line(start, end):
	"""Bresenham's Line Algorithm
	Produces a list of tuples from start and end

	>>> points1 = get_line((0, 0), (3, 4))
	>>> points2 = get_line((3, 4), (0, 0))
	>>> assert(set(points1) == set(points2))
	>>> print points1
	[(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
	>>> print points2
	[(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
	"""
	# Setup initial conditions
	x1, y1 = start
	x2, y2 = end
	dx = x2 - x1
	dy = y2 - y1

	# Determine how steep the line is
	is_steep = abs(dy) > abs(dx)

	# Rotate line
	if is_steep:
		x1, y1 = y1, x1
		x2, y2 = y2, x2

	# Swap start and end points if necessary and store swap state
	swapped = False
	if x1 > x2:
		x1, x2 = x2, x1
		y1, y2 = y2, y1
		swapped = True

	# Recalculate differentials
	dx = x2 - x1
	dy = y2 - y1

	# Calculate error
	error = int(dx / 2.0)
	ystep = 1 if y1 < y2 else -1

	# Iterate over bounding box generating points between start and end
	y = y1
	points = []
	for x in range(x1, x2 + 1):
		coord = (y, x) if is_steep else (x, y)
		points.append(coord)
		error -= abs(dy)
		if error < 0:
			y += ystep
			error += dx

	# Reverse the list if the coordinates were swapped
	if swapped:
		points.reverse()
	return points


def SimpleReflexBoss(bossSprt, table): # reglas, retorna acciones

	# Colisiones con muros
	if bossSprt.collideUp or bossSprt.collideDown or bossSprt.collideRight or bossSprt.collideLeft:

		if bossSprt.collideUp:
			table['movDown'] = True
		if bossSprt.collideDown:
			table['movUp'] = True
		if bossSprt.collideRight:
			table['movLeft'] = True
		if bossSprt.collideLeft:
			table['movRight'] = True

	# Colisiones con objetos
	elif bossSprt.collideObjectUp or bossSprt.collideObjectDown or bossSprt.collideObjectRight or bossSprt.collideObjectLeft:
		bossSprt.last_chase = pg.time.get_ticks()
		bossSprt.chase = 0

		if bossSprt.collideObjectUp:
			if bossSprt.rand == 1:
				table['movLeft'] = True
			else:
				table['movRight'] = True
		if bossSprt.collideObjectDown:
			if bossSprt.rand == 1:
				table['movLeft'] = True
			else:
				table['movRight'] = True

		if bossSprt.collideObjectLeft:
			if bossSprt.rand == 1:
				table['movUp'] = True
			else:
				table['movDown'] = True
		if bossSprt.collideObjectRight:
			if bossSprt.rand == 1:
				table['movUp'] = True
			else:
				table['movDown'] = True
		else:
			pass

	# Si no hay colisiones, persigue al jugador a muerte
	if(bossSprt.chase == 1):
	# else:
		if bossSprt.jp.rect.x > bossSprt.rect.x :
			table['movRight'] = True
		if bossSprt.jp.rect.x < bossSprt.rect.x:
			table['movLeft'] = True
		if bossSprt.jp.rect.y > bossSprt.rect.y:
			table['movDown'] = True
		if bossSprt.jp.rect.y < bossSprt.rect.y:
			table['movUp'] = True
		else:
			pass


	# Ataque simple
	if abs(bossSprt.rect.x - bossSprt.jp.rect.x) > 200 or abs(bossSprt.rect.y - bossSprt.jp.rect.y) > 200 :
		if bossSprt.atk == 0:
			table['long'] = True
			bossSprt.atk = 1
			bossSprt.last_atk = pg.time.get_ticks()
	else:
		table['short'] = True

	return table


class Boss (pg.sprite.Sprite):
	jp=None
	ls_muros = None
	ls_block = None
	ls_proy = None
	def __init__(self,archivo,a,b):
		pg.sprite.Sprite.__init__(self)
		self.m = archivo
		self.image=self.m[a][b]
		self.a = a
		self.b = b
		self.i = b
		self.dir = a
		self.rect=self.image.get_rect()
		self.rect.x= 200
		self.rect.y= 500
		self.keys=pg.key.get_pressed()

		self.cd_rand=1000
		self.last_rand=pg.time.get_ticks()
		self.rand = random.randint(0,1)

		# Banderas y tempos
		self.band = 1 # Para la animacion
		self.staph = 0
		self.cd_staph = 80
		self.last_staph = pg.time.get_ticks()

		self.chase = 1
		self.cd_chase = 100
		self.last_chase = pg.time.get_ticks()
		self.col = 0
		self.cd_col = 100
		self.last_col = pg.time.get_ticks()


		# muros
		self.collideUp=False
		self.collideDown=False
		self.collideRight=False
		self.collideLeft=False

		# Objetos
		self.collideObjectUp = False
		self.collideObjectDown = False
		self.collideObjectRight = False
		self.collideObjectLeft = False

		self.collidePlayer=False

		self.table = {'movUp':False, 'movDown':False, 'movRight':False, 'movLeft':False,'attack':False, 'short': False, 'long': False}

		self.atk = 0
		self.cd_atk = 5000
		self.last_atk = pg.time.get_ticks()

	def move(self,dx,dy):
		if dx != 0:
			self.collide(dx, 0)
		if dy != 0:
			self.collide(0, dy)
		if self.staph == 0:
			self.staph = 1
			self.animate(dx, dy)

	def collide(self,dx,dy):
		self.rect.x+=dx
		self.rect.y+=dy

		self.collidePlayer=False

		self.collideUp=False
		self.collideDown=False
		self.collideRight=False
		self.collideLeft=False

		ls_golpes = pg.sprite.spritecollide(self,self.ls_muros,False)
		for g in ls_golpes:
			if dx>0:
				# self.rect.right = g.rect.left
				self.collideRight = True
			if dx<0:
				# self.rect.left = g.rect.right
				self.collideLeft = True
			if dy>0:
				# self.rect.bottom = g.rect.top
				self.collideDown = True
			if dy<0:
				# self.rect.top = g.rect.bottom
				self.collideUp = True

		self.collideObjectUp=False
		self.collideObjectDown=False
		self.collideObjectRight=False
		self.collideObjectLeft=False


		ls_golpes = pg.sprite.spritecollide(self,self.ls_block,False)
		for g in ls_golpes:
			if dx>0:
				self.rect.right = g.rect.left
				self.collideObjectRight=True
			if dx<0:
				self.rect.left = g.rect.right
				self.collideObjectLeft=True
			if dy>0:
				self.rect.bottom = g.rect.top
				self.collideObjectDown= True
			if dy<0:
				self.rect.top = g.rect.bottom
				self.collideObjectUp= True

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

	def shoot(self):
		pend = abs((self.rect.y - self.jp.rect.y)/(self.rect.x - self.jp.rect.x))
		if pend > 1:
			cantPuntos = abs(self.rect.y - self.jp.rect.y)
		else:
			cantPuntos = abs(self.rect.x - self.jp.rect.x)
		cantPuntos = int(cantPuntos/10) #velocidad proyectiles; cantidad de ciclos hasta que el proyectil llegue al fin

		#Ajuste predice la posicion del jugador en 8 rectas el +16 es solo para centrar el target
		if self.keys[pg.K_a] and self.keys[pg.K_s]:
			ajustex=-self.jp.velocidad*cantPuntos
			ajustey=self.jp.velocidad*cantPuntos
			b=Disparo('fish.png', self.rect.x, self.rect.y, (self.jp.rect.x+ajustex+16,self.jp.rect.y+ajustey+16))
			self.ls_proy.add(b)
			return
		if self.keys[pg.K_d] and self.keys[pg.K_s]:
			ajustex=self.jp.velocidad*cantPuntos
			ajustey=self.jp.velocidad*cantPuntos
			b=Disparo('fish.png', self.rect.x, self.rect.y, (self.jp.rect.x+ajustex+16,self.jp.rect.y+ajustey+16))
			self.ls_proy.add(b)
			return
		if self.keys[pg.K_a] and self.keys[pg.K_w]:
			ajustex=-self.jp.velocidad*cantPuntos
			ajustey=-self.jp.velocidad*cantPuntos
			b=Disparo('fish.png', self.rect.x, self.rect.y, (self.jp.rect.x+ajustex+16,self.jp.rect.y+ajustey+16))
			self.ls_proy.add(b)
			return
		if self.keys[pg.K_d] and self.keys[pg.K_w]:
			ajustex=self.jp.velocidad*cantPuntos
			ajustey=-self.jp.velocidad*cantPuntos
			b=Disparo('fish.png', self.rect.x, self.rect.y, (self.jp.rect.x+ajustex+16,self.jp.rect.y+ajustey+16))
			self.ls_proy.add(b)
			return
		if self.keys[pg.K_a]:
			ajustex=-self.jp.velocidad*cantPuntos
			b=Disparo('fish.png', self.rect.x, self.rect.y, (self.jp.rect.x+ajustex+16,self.jp.rect.y+16))
			self.ls_proy.add(b)
			return
		if self.keys[pg.K_d]:
			ajustex=self.jp.velocidad*cantPuntos
			b=Disparo('fish.png', self.rect.x, self.rect.y, (self.jp.rect.x+ajustex+16,self.jp.rect.y+16))
			self.ls_proy.add(b)
			return
		if self.keys[pg.K_w]:
			ajustey=-self.jp.velocidad*cantPuntos
			b=Disparo('fish.png', self.rect.x, self.rect.y, (self.jp.rect.x+16,self.jp.rect.y+ajustey+16))
			self.ls_proy.add(b)
			return
		if self.keys[pg.K_s]:
			ajustey=self.jp.velocidad*cantPuntos
			b=Disparo('fish.png', self.rect.x, self.rect.y, (self.jp.rect.x+16,self.jp.rect.y+ajustey+16))
			self.ls_proy.add(b)
			return


	def update(self):
		# if self.jp.rect.x-self.rect.x <= 32 and self.jp.rect.y-self.rect.y <= 32:
		#	 self.collidePlayer = True
		# else:
		#	 self.collidePlayer = False
		self.keys=pg.key.get_pressed()
		if self.chase != 0:
			self.table = {'movUp':False, 'movDown':False, 'movRight':False, 'movLeft':False,'attack':False, 'short': False, 'long': False}

		# Temporizadores
		now=pg.time.get_ticks()
		if now - self.last_rand >= self.cd_rand:
			self.rand=random.randint(0,1)
			self.last_rand=now

		if now - self.last_chase >= self.cd_chase:
			self.chase = 1
			self.last_chase=now

		if now - self.last_atk >= self.cd_atk:
			self.atk = 0
			self.last_atk = now

		if now - self.last_staph >= self.cd_staph:
			self.staph = 0
			self.last_staph = now

		action = SimpleReflexBoss(self, self.table)

		if action['movUp']:
			self.move(0,-2)
			self.dir = 3
		if action['movDown']:
			self.move(0,2)
			self.dir = 0
		if action['movRight']:
			self.move (2,0)
			self.dir = 2
		if action['movLeft']:
			self.move (-2,0)
			self.dir = 1
		if action['short']:
			self.jp.hp -= 1
		if action['long']:
			self.shoot()
			# print '*************Disparo*****************'

class Disparo(pg.sprite.Sprite):
	def __init__(self,archivo,x,y,direccion):
		pg.sprite.Sprite.__init__(self)
		self.dir=direccion
		self.image=pg.image.load(archivo).convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.actual=0
		self.list=get_line((self.rect.x,self.rect.y),direccion)
		self.reached=False
		self.vel=10
	def update(self):
		if self.actual+self.vel>= len(self.list)-1:
			self.reached=True
		if not self.reached:
			self.actual+=self.vel
			self.rect.x=self.list[self.actual][0]
			self.rect.y=self.list[self.actual][1]
		else:
			self.kill()
