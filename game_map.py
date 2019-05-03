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


def generate_map(game):
	terrain_sprites = arcade.SpriteList()
	map_infos = get_map_from_owners(game.terrain_owners)

	for (index, value) in enumerate(map_infos):
		(x, y) = get_grid_coords(index)

		owner = value['player']

		if owner is not None:

			# if owner == 1:
			# 	Terrain = textures.ENERGY.fire
			# elif owner == 2:
			# 	Terrain = textures.ENERGY.plant
			if owner not in [1, 2, 3, 4]:
				raise ValueError(
				    f"OWNER OF CASE `{index}` is `{owner}`, it is not known!")

			energy = sprites.Terrain(
			    textures=game.terrain_textures, Terrain=owner, x=x, y=y)
			terrain_sprites.append(energy)

		else:
			empty = sprites.Terrain(
			    textures=game.terrain_textures,
			    Terrain=textures.EMPTY,
			    x=x,
			    y=y)
			terrain_sprites.append(empty)

	return terrain_sprites


def get_map_from_owners(cases):
	game_map = []
	for case in cases:
		game_map.append({'player': case, 'process': None})
	return game_map