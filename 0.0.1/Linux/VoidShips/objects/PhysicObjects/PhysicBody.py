import pygame as pg
from PhysicsEngine import *
from settings import *

class PhysicBody(pg.sprite.Sprite):
    def __init__(self, game, x, y, groups):
        self.groups = groups, game.physic_objects
        pg.sprite.Sprite.__init__(self, groups)
        self.game = game
        self.type = type
        self.pos = vec(x, y) * TILESIZE
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pos = vec(x, y) * TILESIZE
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.tilepos = (int(self.pos.x / TILESIZE), int(self.pos.y / TILESIZE))
        self.chunkpos = (int(self.tilepos[0] / CHUNKSIZE), int(self.tilepos[1] / CHUNKSIZE))
