import random
import pygame as pg


tempo = 0
last_tempo = pg.time.get_ticks()
cd_tempo = 5000

def TableDrivenBoss(bossSprt):
    table = {((bossSprt.jp.rect.x > bossSprt.rect.x),): 'movRight'}



def SimpleReflexBoss(bossSprt, table): #reglas, retorna acciones

    if bossSprt.collidePlayer:
        table['attack'] = True

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

        if bossSprt.collideObjectUp or bossSprt.collideObjectDown:
            if bossSprt.jp.rect.x > bossSprt.rect.x :
                table['movRight'] = True
            elif bossSprt.jp.rect.x < bossSprt.rect.x:
                table['movLeft'] = True

        elif bossSprt.collideObjectLeft or bossSprt.collideObjectRight:
            if bossSprt.jp.rect.y > bossSprt.rect.y:
                table['movDown'] = True
            elif bossSprt.jp.rect.y < bossSprt.rect.y:
                table['movUp'] = True

    # Si no hay colisiones, persigue al jugador a muerte
    elif(bossSprt.chase == 1):
    # else:
        if bossSprt.jp.rect.x > bossSprt.rect.x :
            table['movRight'] = True
        if bossSprt.jp.rect.x < bossSprt.rect.x:
            table['movLeft'] = True
        if bossSprt.jp.rect.y > bossSprt.rect.y:
            table['movDown'] = True
        if bossSprt.jp.rect.y < bossSprt.rect.y:
            table['movUp'] = True
    return table


class Boss (pg.sprite.Sprite):
    jp=None
    ls_muros = None
    ls_block = None
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

        self.cd_rand=20000
        self.last_rand=pg.time.get_ticks()
        self.rand = random.randint(0,1)

        # Banderas y tempos
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

        self.table = {'movUp':False, 'movDown':False, 'movRight':False, 'movLeft':False,'attack':False}

    def move(self,dx,dy):
        if dx != 0:
            self.collide(dx, 0)
        if dy != 0:
            self.collide(0, dy)

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

    def update(self):
        # if self.jp.rect.x-self.rect.x <= 32 and self.jp.rect.y-self.rect.y <= 32:
        #     self.collidePlayer = True
        # else:
        #     self.collidePlayer = False

        if self.chase != 0:
            self.table = {'movUp':False, 'movDown':False, 'movRight':False, 'movLeft':False,'attack':False}
        now=pg.time.get_ticks()
        if now - self.last_rand >= self.cd_rand:
            self.rand=random.randint(0,1)
            self.last_rand=now

        if now - self.last_col >= self.cd_col:
            self.col = 0
            self.last_col = now

        if now - self.last_chase >= self.cd_chase:
            self.chase = 1
            self.last_chase=now

        action = SimpleReflexBoss(self, self.table)

        if action['movUp']:
            self.move(0,-1)
            self.dir = 3
        if action['movDown']:
            self.move(0,1)
            self.dir = 0
        if action['movRight']:
            self.move (1,0)
            self.dir = 2
        if action['movLeft']:
            self.move (-1,0)
            self.dir = 1
        if action['attack']:
            self.jp.hp -= 1
