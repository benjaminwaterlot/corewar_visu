import arcade
import const


class ENERGY():
	fire = 1
	plant = 2
	water = 3
	electricity = 4


# energies = ["fire", "plant", "water", "electricity"]


class Pokemon():
	def __init__(self):
		print("INITIALIZING POKEMONS")


EMPTY = 0


def load_terrain_textures():
	loaded = []
	terrains = [
	    "resources/empty.png", "resources/energies/fire.png",
	    "resources/energies/plant.png", "resources/energies/water.png",
	    "resources/energies/electricity.png"
	]

	for terrain in terrains:
		loaded.append(arcade.load_texture(terrain))
	return loaded


def load_big_pokemon_textures():
	loaded = []
	pokemons = [champion['pokemon'] for champion in const.CHAMPIONS]
	for pokemon in pokemons:
		loaded.append(arcade.load_texture(pokemon))
	return loaded
