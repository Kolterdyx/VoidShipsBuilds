import pygame as pg
from settings import *


class Camera:
	def __init__(self, width, height, game):
		self.camera = pg.Rect(0, 0, width, height)
		self.width = width
		self.height = height
		self.game = game

	def apply(self, entity):
		return entity.rect.move(self.camera.topleft)

	def apply_rect(self, rect):
		return rect.move(self.camera.topleft)

	def update(self, target):
		x = -target.rect.x + int(self.game.WIDTH / 2)
		y = -target.rect.y + int(self.game.HEIGHT / 2)

		# # limit scrolling to map size (limited map)
		# x = min(0, x)  # left
		# y = min(0, y)  # top
		# x = max(-(self.width - WIDTH), x)  # right
		# y = max(-(self.height - HEIGHT), y)  # bottom

		self.camera = pg.Rect(x, y, self.width, self.height)
