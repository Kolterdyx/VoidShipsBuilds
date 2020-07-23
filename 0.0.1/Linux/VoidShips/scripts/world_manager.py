import random
from settings import *


# NOISE GENERATOR ---------------------------------------------------------------

def perlin_noise(x, y, z):
	X = int(x) & 255				  # FIND UNIT CUBE THAT
	Y = int(y) & 255				  # CONTAINS POINT.
	Z = int(z) & 255
	x -= int(x)								# FIND RELATIVE X,Y,Z
	y -= int(y)								# OF POINT IN CUBE.
	z -= int(z)
	u = fade(x)								# COMPUTE FADE CURVES
	v = fade(y)								# FOR EACH OF X,Y,Z.
	w = fade(z)
	A = p[X  ]+Y; AA = p[A]+Z; AB = p[A+1]+Z	  # HASH COORDINATES OF
	B = p[X+1]+Y; BA = p[B]+Z; BB = p[B+1]+Z	  # THE 8 CUBE CORNERS,

	return lerp(w, lerp(v, lerp(u, grad(p[AA  ], x  , y  , z   ),  # AND ADD
								   grad(p[BA  ], x-1, y  , z   )), # BLENDED
						   lerp(u, grad(p[AB  ], x  , y-1, z   ),  # RESULTS
								   grad(p[BB  ], x-1, y-1, z   ))),# FROM  8
				   lerp(v, lerp(u, grad(p[AA+1], x  , y  , z-1 ),  # CORNERS
								   grad(p[BA+1], x-1, y  , z-1 )), # OF CUBE
						   lerp(u, grad(p[AB+1], x  , y-1, z-1 ),
								   grad(p[BB+1], x-1, y-1, z-1 ))))

def fade(t):
	return t ** 3 * (t * (t * 6 - 15) + 10)

def lerp(t, a, b):
	return a + t * (b - a)

def grad(hash, x, y, z):
	h = hash & 15					  # CONVERT LO 4 BITS OF HASH CODE
	u = x if h<8 else y				# INTO 12 GRADIENT DIRECTIONS.
	v = y if h<4 else (x if h in (12, 14) else z)
	return (u if (h&1) == 0 else -u) + (v if (h&2) == 0 else -v)

p = [None] * 512
permutation = [151,160,137,91,90,15,
   131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
   190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
   88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
   77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
   102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
   135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
   5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
   223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
   129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
   251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
   49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
   138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]
for i in range(256):
	p[256+i] = p[i] = permutation[i]

def noise(x, y, seed):
	return float("%1.17f" % perlin_noise(seed/10, x, y))

# ---------------------------------------------------------------------------------


class WorldManager():

	def __init__(self, game, data, seed, name="Empty"):

		self.game = game
		self.loaded = []
		self.chunk = tuple()
		self.unsaved = int()
		if seed:
			self.seed = int(seed)
		else:
			self.seed = int(seedgen)
		if name == "" or not name:
			self.name = DEFAULT_WORLD_NAME
		else:
			self.name = name
		self.chunks = data

	def get_seed(self):
		return int(self.seed)

	def get_name(self):
		return self.name

	def get_chunks(self):
		return self.chunks

	def get_loaded(self):
		return self.loaded

	# remove given chunk from the loaded list, so it does not affect the performance
	def unload(self, chunk):
		self.loaded.remove(chunk)

	def kill_item(self, chunk, pos):
		if self.chunks[chunk]["items"][pos]:
			del self.chunks[chunk]["items"][pos]
		else:
			print("Item does not exist")
			pass

	def change_block(self, chunk, pos, type):
		if self.chunks[chunk]["floor"][pos]:
			self.chunks[chunk]["floor"][pos] = type
		else:
			print("Block does not exist")
			pass

	# Generate a chunk at given coordinates using pnoise2 and adding it to the chunk list
	def generate(self, chunkx, chunky):

		# print("Generating chunk at", chunkx, chunky)

		GRASS = "grass"
		MOUNTAIN = "mountain"
		EMPTY = "void"

		floor_void_diff = 0.3
		mountain = floor_void_diff + 0.27

		factor = 15

		floor = {}
		items = {}
		chunk = (chunkx, chunky)

		if chunk not in self.chunks:

			# print("Generating chunk at {}".format(chunk))
			for y in range(chunky * CHUNKSIZE, chunky * CHUNKSIZE + CHUNKSIZE):
				for x in range(chunkx * CHUNKSIZE, chunkx * CHUNKSIZE + CHUNKSIZE):
					i = noise(x/factor, y/factor, int(self.seed))
					if i >= floor_void_diff:
						if i > mountain:
							floor.update({(x, y): MOUNTAIN})
						else:
							floor.update({(x, y): GRASS})
						spawner = random.randint(-1, ITEM_SPAWN_RATIO)
						random_item = random.randint(0, len(ITEM_LIST)-1)

						if spawner == 0:
							items.update({(x, y): ITEM_LIST[random_item]})

					elif i < floor_void_diff:
						floor.update({(x, y): EMPTY})
					else:
						floor.update({(x, y): EMPTY})

			self.chunks.update({chunk: {"floor": floor, "items": items}})
			self.unsaved += 1
		# else:
		# 	print("Chunk at {} has already been generated".format(chunk))

	# Saving generated chunks list to a file, so it can be loaded from there rather than re-generating everything again
	def save(self):
		if self.unsaved == 0:
			print("Nothing needs to be saved")
			self.unsaved = 0
		else:
			if self.unsaved == 1:
				pass
				# print("Saved {} chunk".format(self.unsaved))
			else:
				pass
				# print("Saved {} chunks".format(self.unsaved))
			self.unsaved = 0
		return self.chunks

	# Load chunk at given coordinates
	def load(self, chunkx, chunky):
		chunk = (chunkx, chunky)

		if chunk not in self.chunks:
			print("Chunk at {} does not exist".format(cname))
		else:
			if chunk not in self.loaded:

				# Add the chunk to the loaded chunks list
				self.loaded.append(chunk)
				# print("Loading chunk at {}".format(cname))
				data = []
				floordata = []
				itemdata = []

				# Select the chunk acording to the coordinates given
				chunktoload = self.chunks[chunk]

				# Generate a data bundle so it can be passed to the map loader
				for index, type in enumerate(chunktoload):
					if type == "floor":
						for tile in chunktoload["floor"]:
							floordata.append((chunktoload["floor"][tile], tile[0], tile[1]))

					if type == "items":
						for item in chunktoload["items"]:
							itemdata.append((chunktoload["items"][item], item[0], item[1]))

				data = [floordata, itemdata]
				return data

			else:
				# print("Chunk at {} has already been loaded".format(cname))
				pass
