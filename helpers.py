import const


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


def process_counter(game):
	pass