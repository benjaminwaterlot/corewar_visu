import arcade
import sprites
import textures


def generate_map(game):
	GRID_X = 85
	POKEMON_SIZE = 24
	map_sprites = arcade.SpriteList()
	# images = [
	#     "energies/fire.png", "energies/plant.png", "pokemons/bulbizarre.png",
	#     "pokemons/salameche.png"
	# ]
	# textures = map(lambda x: f"resources/{x}", images)

	# map_sprites.preload_textures(textures)

	map_infos = get_map_from_owners(game.map_owners)

	for (index, value) in enumerate(map_infos):
		x = game.MARGIN * 2 + index * POKEMON_SIZE % (GRID_X * POKEMON_SIZE)
		y = game.SCREEN_HEIGHT - 200 - int(index / GRID_X) * POKEMON_SIZE

		empty = sprites.energy(energy_type=textures.empty, x=x, y=y)
		map_sprites.append(empty)

		owner = value['player']
		process = value['process']
		if process is not None:
			if process == 1:
				pokemon_type = textures.salameche
			elif process == 2:
				pokemon_type = textures.bulbizarre
			else:
				raise ValueError(
				    f"OWNER OF CASE `{index}` is `{process}`, it is not known!"
				)
			pokemon = sprites.energy(
			    energy_type=pokemon_type, id=None, x=x, y=y)
			map_sprites.append(pokemon)
		elif owner is not None:
			if owner == 1:
				energy_type = textures.fire
			elif owner == 2:
				energy_type = textures.plant
			else:
				raise ValueError(
				    f"OWNER OF CASE `{index}` is `{owner}`, it is not known!")
			energy = sprites.energy(energy_type, x, y)
			map_sprites.append(energy)

	return map_sprites


def get_map_from_owners(cases):
	game_map = []
	for case in cases:
		game_map.append({
		    'player': None if case is 'x' else int(case),
		    'process': None
		})
		# if i < 390:
		# 	game_map.append({'player': 1, 'process': None})
		# elif i == 390:
		# 	game_map.append({'player': 1, 'process': 1})
		# elif i == 3200 + 390:
		# 	game_map.append({'player': 2, 'process': 2})
		# elif i > 3200 and i < 3200 + 390:
		# 	game_map.append({'player': 2, 'process': None})
		# else:
		# 	game_map.append({'player': None, 'process': None})
	return game_map