def fps_logger(game, delta_time):
	game.frame += 1
	if (not game.frame % 30):
		print(f"▷  Cycle {game.cycle} : FPS: {round(1 / delta_time)}")
		print(f"UPDATES COUNT: P: {game.P_count}, M: {game.M_count}")
