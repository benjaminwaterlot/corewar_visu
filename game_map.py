import arcade
import sprites
import const
from textures import ENERGY, POKEMON, EMPTY


def get_grid_coords(index):
	x = const.MARGIN * 2 + index * const.POKEMON_SIZE % (
	    const.GRID_X * const.POKEMON_SIZE)
	y = const.SCREEN_HEIGHT - 200 - int(
	    index / const.GRID_X) * const.POKEMON_SIZE
	return (x, y)


def generate_map(game):
	map_sprites = arcade.SpriteList()

	map_infos = get_map_from_owners(game.map_owners)
	# print(game.textures)

	for (index, value) in enumerate(map_infos):
		(x, y) = get_grid_coords(index)

		owner = value['player']
		process = value['process']

		if process is not None:
			if process == 1:
				pokemon_type = POKEMON.salameche
			elif process == 2:
				pokemon_type = POKEMON.bulbizarre
			else:
				raise ValueError(
				    f"OWNER OF CASE `{index}` is `{process}`, it is not known!"
				)
			pokemon = sprites.entity(
			    textures=game.textures, entity=pokemon_type, x=x, y=y)
			map_sprites.append(pokemon)

		elif owner is not None:
			if owner == 1:
				entity = ENERGY.fire
			elif owner == 2:
				entity = ENERGY.plant
			else:
				raise ValueError(
				    f"OWNER OF CASE `{index}` is `{owner}`, it is not known!")
			energy = sprites.entity(
			    textures=game.textures, entity=entity, x=x, y=y)
			map_sprites.append(energy)

		else:
			empty = sprites.entity(
			    textures=game.textures, entity=EMPTY, x=x, y=y)
			map_sprites.append(empty)

	for process in game.processes:
		print(process)
		map_sprites[process['location']].set_texture(POKEMON.bulbizarre - 1 +
		                                             process['champion'])

	return map_sprites


def get_map_from_owners(cases):
	game_map = []
	for case in cases:
		game_map.append({'player': case, 'process': None})
	return game_map