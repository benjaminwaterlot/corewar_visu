import arcade
import const
import random
from helpers import get_grid_coords


class Terrain(arcade.Sprite):
	def __init__(self, ref, x, y, visible=True):
		super().__init__()

		for texture in const.TERRAIN_TEXTURES:
			self.textures.append(texture)

		self.id = id
		self.set_texture(ref)
		self.scale = 1
		self.center_x = x
		self.center_y = y
		self.alpha = 255 if visible else 0


class Live(arcade.Sprite):
	def __init__(self, champion, live_len):
		super().__init__()

		self.textures.append(const.CHAMPIONS[champion - 1]['energy'])
		self.set_texture(0)

		self.scale = 1

		self.center_x = const.SCREEN_WIDTH - 400
		self.center_y = const.SCREEN_HEIGHT - 100 - live_len * 16

		self.champion = champion


class pokemon(arcade.Sprite):
	def __init__(self, texture, location, champion):
		super().__init__()

		self.textures.append(texture)
		self.set_texture(0)
		self.scale = 1.2
		(self.center_x, self.center_y) = get_grid_coords(location)
		self.champion = champion


class EndPokemon(arcade.Sprite):
	def __init__(self, texture, x, y):
		super().__init__()

		self.textures.append(texture)
		self.set_texture(0)
		self.scale = 1.2
		(self.center_x, self.center_y) = (x, y)


class Big_Pokemon(arcade.Sprite):
	def __init__(self, texture, coords):
		super().__init__()

		self.textures.append(texture)
		self.set_texture(0)
		self.scale = 1
		(self.center_x, self.center_y) = coords