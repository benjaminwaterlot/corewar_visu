import arcade
from helpers import get_grid_coords

# def energy(energy_type, x, y):
# 	return arcade.Sprite(
# 	    filename=f"resources/energies/{energy_type}.png",
# 	    scale=1,
# 	    center_x=x,
# 	    center_y=y)


class Terrain(arcade.Sprite):
	def __init__(self, textures, Terrain, x, y):
		super().__init__()
		# texture = arcade.load_texture(
		#     f"resources/energies/{Terrain}.png", scale=1)

		# textures_loaded = arcade.load_textures(textures)
		for texture in textures:
			# texture_loaded = arcade.load_texture(file_name=texture)
			self.textures.append(texture)
		# self.textures.append(textures)

		self.id = id
		# self.textures.append(texture)
		self.set_texture(Terrain)
		self.scale = 1
		self.center_x = x
		self.center_y = y
		# if Terrain == 0:
		# self.alpha = 0


class pokemon(arcade.Sprite):
	def __init__(self, texture, location):
		super().__init__()
		# texture = arcade.load_texture(
		#     f"resources/energies/{Terrain}.png", scale=1)

		self.textures.append(texture)
		self.set_texture(0)
		self.scale = 1.2
		(self.center_x, self.center_y) = get_grid_coords(location)
		# self.alpha = 0


# class pokemon(arcade.Sprite):
# 	def __init__(self, pokemon_type, id, x, y):
# 		super().__init__()
# 		texture = arcade.load_texture(
# 		    f"resources/pokemons/{pokemon_type}.png", mirrored=True, scale=1)
# 		self.id = id
# 		self.textures.append(texture)
# 		self.set_texture(0)
# 		self.scale = 1
# 		self.center_x = x
# 		self.center_y = y

# def empty(x, y):
# 	return arcade.Sprite(
# 	    filename=f"resources/empty.png", scale=.6, center_x=x, center_y=y)
