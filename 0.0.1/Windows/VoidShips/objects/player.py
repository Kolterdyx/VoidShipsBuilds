import pygame as pg
from settings import *
from settings import collide_hit_rect
from textures import *
from PhysicObjects import *

class Player(KinematicBody):
	def __init__(self, game, x, y):
		self._layer = PLAYER_LAYER
		self.groups = game.all_sprites
		KinematicBody.__init__(self, game, x, y, self.groups)
		self.img = PLAYER_IMG
		self.image = self.img
		self.rect = self.image.get_rect()
		self.hit_rect = PLAYER_HITRECT
		self.hitrect_offset = 12
		self.name = PLAYER_DEFAULT_NAME
		self.on_inv = false
		self.holding = null
		self.hotbar_display = {
			0: null,
			1: null,
			2: null
		}
		self.inv_display = {
			0: null,
			1: null,
			2: null,
			3: null,
			4: null,
			5: null,
			6: null,
			7: null,
			8: null
		}
		self.selected_slot = 0
		# Create new inventory ──────────────────────────────────────────────────────────────────────────
		self.selected_slot = 0
		self.fullinv = DEFAULT_WORLD_FORMAT["player"]["fullinv"]
		self.acc = vec(0, 0)
		self.vel = vec(0, 0)
		self.friction = vec(5, 5)
		self.applied_force = vec(0,0)
		self.applied_impulse = vec(0,0)
	# Load the data passed from the create() function in main.py

	def load_data(self, data):
		self.playerdata = data
		self.pos = vec(data["pos"])
		self.tilepos = vec(int(self.pos.x / TILESIZE), int(self.pos.y / TILESIZE))
		self.chunkpos = self.tilepos * CHUNKSIZE
		self.name = data["name"]
		# Load inventory ────────────────────────────────────────────────────────────────────────────────
		self.selected_slot = data["selected_slot"]
		self.fullinv = data["fullinv"]
	# Save the player"s data

	def save_data(self):
		# print("Saving player data")
		self.playerdata.update({
			"pos": tuple(self.pos),
			"name": self.name,
			"selected_slot": self.selected_slot,
			"fullinv": self.fullinv
		})
		return self.playerdata
	# Get input for player movement

	def get_keys(self):
		keys = pg.key.get_pressed()
		self.vel = vec(0, 0)
		if not self.on_inv:
			if keys[pg.K_a]:
				self.vel.x = -PLAYER_SPEED
			if keys[pg.K_d]:
				self.vel.x = PLAYER_SPEED
			if keys[pg.K_w]:
				self.vel.y = -PLAYER_SPEED
			if keys[pg.K_s]:
				self.vel.y = PLAYER_SPEED
			if self.vel.x != 0 and self.vel.y != 0:
				self.vel *= 0.7071
	# Update the player values

	def update(self):

		self.get_keys()
		self.move_and_collide(self.vel)

		# Flip the player's image depending on its velocity
		if self.vel.x < 0:
			self.image = pg.transform.flip(self.img, true, false)
		if self.vel.x > 0:
			self.image = self.img
