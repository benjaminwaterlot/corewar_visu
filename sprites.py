import arcade
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


class pokemon(arcade.Sprite):
	def __init__(self, texture, location):
		super().__init__()

		self.textures.append(texture)
		self.set_texture(0)
		self.scale = 1.2
		(self.center_x, self.center_y) = get_grid_coords(location)


class Big_Pokemon(arcade.Sprite):
	def __init__(self, texture, coords):
		super().__init__()

		self.textures.append(texture)
		self.set_texture(0)
		self.scale = 1
		(self.center_x, self.center_y) = coords