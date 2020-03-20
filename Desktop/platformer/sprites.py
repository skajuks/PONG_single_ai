from settings import *
import pygame as pg


vc = pg.math.Vector2
class Player(pg.sprite.Sprite):

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((30,30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx = 0
        self.vy = 0
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.pos = vc(WIDTH // 2, HEIGHT // 2)
        self.vel = vc(0,0)
        self.acc = vc(0,0)



    def update(self):
        self.acc = vc(0,PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[ord('a')]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT] or keys[ord('d')]:
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x * PLAYER_FRICTION  #friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #wrapper
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def jump(self):
        self.rect.y +=1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -=1
        if hits:
            self.vel.y = -PLAYER_JUMP       

class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(SWAMP)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y