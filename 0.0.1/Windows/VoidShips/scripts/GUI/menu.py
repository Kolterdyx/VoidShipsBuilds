#!/usr/bin/python3.7
import sys
sys.path.insert(0, "/media/kolterdyx/Seagate/Programming/Python/GameDev/VoidShips/")
from textures import *
from scripts import *
from scripts.GUI import *
from settings import*

import pygame as pg

class Menu():
	def __init__(self, game):
		self.game = game
		self.screen = game.screen
		self.display = game.display
		self.font = pg.font.Font("textures/fonts/ttp.otf", 30)
		self.version_font = pg.font.Font("textures/fonts/ttp.otf", 15)
		self.world_name_ask = self.font.render("Enter world name:", 1, (0,0,0))
		self.wne = Entry(self, 20, 100, 750, 30, game.enter_game, "textures/fonts/ttp.otf", 5)
		self.wne.typing = true
		self.button = Button(self, 300, 300, 200, 100, game.enter_game, "Enter", "textures/fonts/ttp.otf", 30)
		self.bgcolor = (100,100,100)
		self.version_label = self.version_font.render("Version: " + str(game.version), 1, (0,0,0))

	def set_bg(self, color):
		self.bgcolor = color

	def run(self):
		try:
			self.screen.fill(self.bgcolor)
			self.screen.blit(self.world_name_ask, (20, 60))
			self.wne.update()
			self.button.update()
			self.screen.blit(self.version_label, (self.display.Info().current_w - self.version_label.get_rect().width - 10, self.display.Info().current_h - self.version_label.get_rect().height - 10))
		except:
			pass


#
# class Screen():
# 	def __init__(self):
# 		pg.init()
# 		self.screen = pg.display.set_mode(SIZE)
# 		self.menu = Menu(self)
#
# 	def run(self):
# 		self.menu.run()
# 		pg.display.flip()
#
# 	def enter_world(self):
# 		print("Entering world:", self.menu.wne.get_text())
#
#
# s = Screen()
# while True:
# 	s.run()
