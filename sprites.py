import arcade


def energy(name, x, y):
	return arcade.Sprite(
	    filename=f"resources/energies/{name}.png",
	    scale=1,
	    center_x=x,
	    center_y=y)


class pokemon(arcade.Sprite):
	def __init__(self, name, x, y):
		super().__init__()
		texture = arcade.load_texture(
		    f"resources/pokemons/{name}.png", mirrored=True, scale=1)
		self.textures.append(texture)
		self.set_texture(0)
		self.scale = 1.5
		self.center_x = x
		self.center_y = y


def empty(x, y):
	return arcade.Sprite(
	    filename=f"resources/empty.png", scale=.6, center_x=x, center_y=y)
