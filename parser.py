import sys


def parse_next():
	data = sys.stdin.readline()
	print(f"{data}")
	# for index, line in sys.stdin:


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
			process = line.split()
			processes.append({'champion': process[1], 'location': process[2]})

		line = sys.stdin.readline().rstrip()

	print(starting_map)
	print(champions)
	print(processes)
	return
