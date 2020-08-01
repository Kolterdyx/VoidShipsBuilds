import pygame as pg
import random
from settings import *
from textures import *


class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, type):
        self._layer = 100
        self.groups = game.obstacles, game.all_sprites, self.hand_breakable
        pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.type = type
		self.image = OBSTACLE[type]
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.pos = vec(x, y) * TILESIZE
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE
		self.tilepos = (int(self.pos.x / TILESIZE), int(self.pos.y / TILESIZE))
		self.chunkpos = (int(self.tilepos[0] / CHUNKSIZE), int(self.tilepos[1] / CHUNKSIZE))
		self.chunkrect = pg.Rect(self.rect.x, self.rect.y, CHUNKTILESIZE, CHUNKTILESIZE)
