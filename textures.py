import arcade


class ENERGY():
	fire = 1
	plant = 2


class Pokemon():
	def __init__(self):
		print("INITIALIZING POKEMONS")


EMPTY = 0


def load_terrain_textures():
	loaded = []
	terrains = [
	    "resources/empty.png", "resources/energies/fire.png",
	    "resources/energies/plant.png"
	]

	for terrain in terrains:
		loaded.append(arcade.load_texture(terrain))
	return loaded


def load_pokemon_textures():
	loaded = []
	pokemons = [
	    "resources/empty.png", "resources/pokemons/salameche.png",
	    "resources/pokemons/bulbizarre.png"
	]
	for pokemon in pokemons:
		loaded.append(arcade.load_texture(pokemon))
	return loaded