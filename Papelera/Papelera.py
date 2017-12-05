while Band_lv1:
	Pj = Pj11

	now = pg.time.get_ticks()

	if now - Pj.last_staph >= Pj.cd_staph:
		Pj.staph = 0
		Pj.last_staph = now

	if now - Pj.last_cansado >= Pj.cd_cansado:
		Pj.cansado = 0
		Pj.last_cansado = now

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

	now2 = pg.time.get_ticks()
	if key[pg.K_SPACE]:
		if Pj.cansado <= 0:
			Pj.cansado = 1000
		else:
			Pj.cansado -= 1
		Pj.velocidad = 5
	else:
		Pj.velocidad = 3

while Band_lv2:
	Pj = Pj12

	now = pg.time.get_ticks()
	if now - Pj.last_staph >= Pj.cd_staph:
		Pj.staph = 0
		Pj.last_staph = now

	if now - Pj.last_cansado >= Pj.cd_cansado:
		Pj.cansado = 0
		Pj.last_cansado = now

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

	now2 = pg.time.get_ticks()
	if key[pg.K_SPACE]:
		if Pj.cansado <= 0:
			Pj.cansado = 1000
		else:
			Pj.cansado -= 1
		Pj.velocidad = 5
	else:
		Pj.velocidad = 3

while Band_lv3:
	Pj = Pj13

	now = pg.time.get_ticks()
	if now - Pj.last_staph >= Pj.cd_staph:
		Pj.staph = 0
		Pj.last_staph = now

	if now - Pj.last_cansado >= Pj.cd_cansado:
		Pj.cansado = 0
		Pj.last_cansado = now

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

	now2 = pg.time.get_ticks()
	if key[pg.K_SPACE]:
		if Pj.cansado <= 0:
			Pj.cansado = 1000
		else:
			Pj.cansado -= 1
		Pj.velocidad = 5
	else:
		Pj.velocidad = 3
