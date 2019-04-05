import arcade
import sprites


def generate_map(game):
	GRID_X = 80
	POKEMON_SIZE = 24
	map_sprites = arcade.SpriteList()

	map_infos = generate_sample_map()
	for (index, value) in enumerate(map_infos):
		x = game.MARGIN * 2 + index * POKEMON_SIZE % (GRID_X * POKEMON_SIZE)
		y = game.SCREEN_HEIGHT - 200 - int(index / GRID_X) * POKEMON_SIZE

		empty = sprites.empty(x, y)
		map_sprites.append(empty)

		owner = value['player']
		process = value['process']
		if process is not None:
			if process == 1:
				name = "salameche"
			elif process == 2:
				name = "bulbizarre"
			else:
				raise ValueError(
				    f"OWNER OF CASE `{index}` is `{process}`, it is not known!"
				)
			pokemon = sprites.pokemon(name, x, y)
			map_sprites.append(pokemon)
		elif owner is not None:
			if owner == 1:
				name = "fire"
			elif owner == 2:
				name = "plant"
			else:
				raise ValueError(
				    f"OWNER OF CASE `{index}` is `{owner}`, it is not known!")
			energy = sprites.energy(name, x, y)
			map_sprites.append(energy)

	return map_sprites


def generate_sample_map():
	game_map = []
	for i in range(3840):
		if i < 390:
			game_map.append({'player': 1, 'process': None})
		elif i == 390:
			game_map.append({'player': 1, 'process': 1})
		elif i == 3200 + 390:
			game_map.append({'player': 2, 'process': 2})
		elif i > 3200 and i < 3200 + 390:
			game_map.append({'player': 2, 'process': None})
		else:
			game_map.append({'player': None, 'process': None})
	return game_map