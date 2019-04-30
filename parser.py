import sys

# from textures import ENERGY, POKEMON, EMPTY


def parse_next(number_to_parse):
	init = sys.stdin.readline().rstrip()

	if init == "":
		print("GAME ENDED")
		exit(0)
	if init[0] != 'C':
		raise ValueError(f"Unexpected input ! [{init}]")

	cycle = [init]
	# for i in range(number_to_parse):
	# 	data = sys.stdin.readline().rstrip()
	# 	while data != "":
	# 		cycle.append(data)
	# 		data = sys.stdin.readline().rstrip()
	for line in sys.stdin:
		if line == "\n":
			number_to_parse -= 1
			if number_to_parse <= 0:
				break
			else:
				continue
		cycle.append(line.rstrip())

	# print(cycle)
	return cycle


def parse_start():
	starting_map = None
	champions = []
	processes = []
	line = sys.stdin.readline().rstrip()

	while line != "":
		print(line)

		if line[0] == 'J':
			champions.append(line.split()[-1])

		elif line[0] == 'B':
			starting_map = line[2:].split()
			print(len(starting_map))

		elif line[0] == 'P':
			(code, ref, location, champion) = line.split()
			# pokemon = POKEMON.salameche if int(
			#     champion) is 1 else POKEMON.bulbizarre
			processes.append({
			    'champion': int(champion),
			    'location': int(location),
			    'pokemon': int(champion)  #TODO = ASSIGNER UN VRAI POKEMON ICI
			})

		line = sys.stdin.readline().rstrip()

	print(starting_map)
	print(champions)
	print(processes)
	return {
	    'starting_map': starting_map,
	    'champions': champions,
	    'processes': processes
	}
