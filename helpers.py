import const
import random


def fps_logger(game, delta_time):
	print(f"▷  Cycle {game.cycle} : FPS: {round(1 / delta_time)}")


def get_grid_coords(index):
	if (index is None):
		raise ValueError(F"INDEX IS NONE !!!!!!!!!!")
	x = const.MARGIN * 2 + index * const.POKEMON_SIZE % (
	    const.GRID_X * const.POKEMON_SIZE)
	y = const.SCREEN_HEIGHT - 200 - int(
	    index / const.GRID_X) * const.POKEMON_SIZE
	return (x, y)


def get_random_pokemon(champion):
	champ = const.CHAMPIONS[champion]
	return random.choice(champ['pokemons'])


def update_lives(lives: list):
	# for live in lives:
	# 	if live > 0:
	# 		live += 1
	# new_lives = [live + 1 if live > 0 and live < 10 else 0 for live in lives]
	# new_lives = [live + 1 if live > 0 and live < 10 else 0 for live in lives]
	return [0, 0, 0, 0]