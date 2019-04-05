import arcade


def energy(energy_type, x, y):
	return arcade.Sprite(
	    filename=f"resources/energies/{energy_type}.png",
	    scale=1,
	    center_x=x,
	    center_y=y)


class pokemon(arcade.Sprite):
	def __init__(self, pokemon_type, id, x, y):
		super().__init__()
		texture = arcade.load_texture(
		    f"resources/pokemons/{pokemon_type}.png", mirrored=True, scale=1)
		self.id = id
		self.textures.append(texture)
		self.set_texture(0)
		self.scale = 1.5
		self.center_x = x
		self.center_y = y


def empty(x, y):
	return arcade.Sprite(
	    filename=f"resources/empty.png", scale=.6, center_x=x, center_y=y)
