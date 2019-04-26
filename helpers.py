def fps_logger(game, delta_time):
	game.frame += 1
	if (not game.frame % 30):
		print(f"▷  Cycle {game.cycle} : FPS: {round(1 / delta_time)}")
