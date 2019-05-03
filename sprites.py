import arcade
import const
import random
from helpers import get_grid_coords


class Terrain(arcade.Sprite):
	def __init__(self, textures, Terrain, x, y):
		super().__init__()

		for texture in textures:
			self.textures.append(texture)

		self.id = id
		self.set_texture(Terrain)
		self.scale = 1
		self.center_x = x
		self.center_y = y


class Live(arcade.Sprite):
	def __init__(self, champion, live_len):
		super().__init__()

		self.textures.append(const.CHAMPIONS[champion - 1]['live'])
		self.set_texture(0)

		randomizer = random.randint(0, 1200)
		little_randomizer = random.randint(0, 20)

		self.scale = 1
		(
		    self.center_x, self.center_y
		) = const.SCREEN_WIDTH - 400, const.SCREEN_HEIGHT - 100 - live_len * 32
		self.champion = champion


class pokemon(arcade.Sprite):
	def __init__(self, texture, location, champion):
		super().__init__()

		self.textures.append(texture)
		self.set_texture(0)
		self.scale = 1.4
		(self.center_x, self.center_y) = get_grid_coords(location)
		self.champion = champion


class Big_Pokemon(arcade.Sprite):
	def __init__(self, texture, coords):
		super().__init__()

		self.textures.append(texture)
		self.set_texture(0)
		self.scale = 1
		(self.center_x, self.center_y) = coords