import arcade


class ENERGY():
	fire = 1
	plant = 2


class Pokemon():
	def __init__(self):
		print("INITIALIZING POKEMONS")


pokemons = [
    "resources/pokemons/salameche.png", "resources/pokemons/bulbizarre.png"
]

EMPTY = 0

images = [
    "resources/empty.png", "resources/energies/fire.png",
    "resources/energies/plant.png"
]


def load_terrain_textures():
	loaded = []
	for texture in images:
		loaded.append(arcade.load_texture(texture))
	return loaded


def load_pokemon_textures():
	loaded = []
	for texture in pokemons:
		loaded.append(arcade.load_texture(texture))
	return loaded