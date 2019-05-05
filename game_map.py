import arcade
import sprites
import const
import textures
from helpers import get_grid_coords
import helpers


def generate_process_sprites(game):
	process_sprites = arcade.SpriteList()

	for process in game.pokemons:
		sprite = sprites.pokemon(
		    helpers.get_random_pokemon(process.champion - 1), process.location,
		    process.champion - 1)
		process_sprites.append(sprite)

	return process_sprites


def get_map_from_owners(cases):
	game_map = []
	for case in cases:
		game_map.append({'player': case, 'process': None})
	return game_map