import pygame as pg
from settings import *
from textures import *

pg.init()

class Button():
	def __init__(self, env, x, y, w, h, func, text, font, font_size):
		self.env = env
		self.rect = pg.Rect((x,y),(w,h))
		self.text = text
		self.func = func
		self.font = pg.font.Font(font, font_size)

		self.font_size = font_size
		self.font_color = (0,0,0)

		self.bgcolor = (255,255,255)
		self.border_width = 5
		self.border = pg.Rect((self.rect.x-self.border_width+2, self.rect.y-self.border_width+2),(w+self.border_width, self.rect.height+self.border_width))
		self.border_color = (0,0,0)

		self.image = pg.Surface((self.rect.size))
		self.image.fill(self.bgcolor)

		self.pressed = False

		self.screen = env.screen

	def set_font_color(self, color):
		self.font_color = color

	def set_bg(self, color):
		self.bgcolor = color
		self.image.fill(color)

	def set_border_width(self, width):
		self.border_width = width

	def set_border_color(self, color):
		self.border_color = color

	def set_text(self, text):
		self.text = text


	def update(self):
		mousepos = pg.mouse.get_pos()
		p1, p2, p3 = pg.mouse.get_pressed()

		if self.rect.collidepoint(mousepos):
			if p1:
				self.pressed = True
				color = (self.bgcolor[0]-20, self.bgcolor[1]-20, self.bgcolor[2]-20)
				self.image.fill(color)
			if not p1 and self.pressed:
				self.pressed = False
				self.func()
				self.image.fill(self.bgcolor)


		self.label = self.font.render(self.text, 1, self.font_color)

		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.label, (self.rect.centerx - self.label.get_rect().width / 2, self.rect.centery - self.label.get_rect().height / 2))
		if self.border_width > 0:
			pg.draw.rect(self.screen, self.border_color, self.border, self.border_width)
