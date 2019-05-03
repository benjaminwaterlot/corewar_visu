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
			    pokemon=const.CHAMPIONS[champ_index]['pokemon'])

			print("PLAYER ADDED TO THE ARENA: ", new_player, "\n")

			champions.append(new_player)

		# elif code == 'J':
		# 	champions.append(line.split()[-1])

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
			# processes.append({
			#     'champion': int(champion),
			#     'location': int(location),
			#     'pokemon': int(champion)  #TODO = ASSIGNER UN VRAI POKEMON ICI
			# })

		line = sys.stdin.readline().rstrip()

	print(champions)
	print(processes)
	return (starting_map, champions, processes)


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
