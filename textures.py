import arcade


class ENERGY():
	fire = 1
	plant = 2


class POKEMON():
	bulbizarre = 3
	salameche = 4


EMPTY = 0

IMAGES = [
    "resources/empty.png", "resources/energies/fire.png",
    "resources/energies/plant.png", "resources/pokemons/bulbizarre.png",
    "resources/pokemons/salameche.png"
]


def get_loaded_textures():
	loaded = []
	for texture in IMAGES:
		loaded.append(arcade.load_texture(texture))
	return loaded