import sys


def parse_next():
	init = sys.stdin.readline().rstrip()

	if init[0] != 'C':
		raise ValueError(f"Unexpected input ! [{init}]")

	cycle = [init]
	data = sys.stdin.readline().rstrip()
	while data != "":
		cycle.append(data)
		data = sys.stdin.readline().rstrip()

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
			processes.append({'champion': champion, 'location': location})

		line = sys.stdin.readline().rstrip()

	print(starting_map)
	print(champions)
	print(processes)
	return {
	    'starting_map': starting_map,
	    'champions': champions,
	    'processes': processes
	}
