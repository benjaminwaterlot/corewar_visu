import sys
import objects
import const


def parse_start():
	starting_map = None
	processes = []
	champions = []
	line = sys.stdin.readline().rstrip()

	while line != "":
		print(line)
		code = line[0]

		if code == '*':
			(_, _, player_id, _, _, _, player_name,
			 *player_desc_raw) = line.split()

			t = " ".join(player_desc_raw)

			try:
				player_desc = t[t.find('(') + 1:t.find(')')]
			except:
				player_desc = ""

			champ_index = int(player_id.replace(',', "")) - 1
			new_player = objects.Champion(
			    id=champ_index,
			    name=player_name.replace('"', ''),
			    description=player_desc,
			    process_count=1,
			    color=const.CHAMPIONS[champ_index]['color'],
			    pokemon=const.CHAMPIONS[champ_index]['pokemon'],
			    big_pokemon=const.CHAMPIONS[champ_index]['big_pokemon'])

			print("PLAYER ADDED TO THE ARENA: ", new_player, "\n")

			champions.append(new_player)

		elif code == 'B':
			starting_map = line[2:].split()
			print(len(starting_map))

		elif code == 'P':
			(_, _, location, champion) = line.split()
			new_process = objects.Process(
			    champion=int(champion),
			    location=int(location),
			    pokemon=int(champion))
			processes.append(new_process)

		line = sys.stdin.readline().rstrip()

	print(champions)
	print(processes)
	return (starting_map, champions, processes)


def parse_next(number_to_parse, game):
	if number_to_parse == 0:
		return []

	init = sys.stdin.readline().rstrip()

	cycle = [init]
	if init[:10] == "Contestant":
		return cycle

	for line in sys.stdin:
		# print(F"{line.rstrip()}")

		if line[0] == "D":
			print(F"CYCLE TO DIE {line}")

		if line[:10] == "Contestant":
			return [line]

		if line == "\n":
			number_to_parse -= 1
		if line == "\n" and number_to_parse < 0:
			break
		if line == "\n" and number_to_parse >= 0:
			continue
		game.parsed += 1
		cycle.append(line.rstrip())

	# print(cycle)
	return cycle
