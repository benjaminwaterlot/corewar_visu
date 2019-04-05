def generate_map():
	game_map = []
	for i in range(3840):
		if i < 390:
			game_map.append(1)
		elif i > 3200 and i < 3200 + 390:
			game_map.append(2)
		else:
			game_map.append(None)
	return game_map