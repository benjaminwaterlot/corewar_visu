# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/17 14:49:38 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/18 15:51:29 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyglet as pyg
import ui.text
import ui.room
# import components
# from components import room as c_room, link as c_link
import components.room
import components.link
# import components.


class App:
	lems = 0
	rooms = []
	links = []
	lem_input = ""
	window = None
	bounds = {
		'x': 0,
		'y': 0,
	}

	def __init__(self, lem_input, window):
		self.lem_input = lem_input
		self.window = window
		self.read_input(lem_input)
		print(f">> NUMBER OF LEMS : `{self.lems}`\n")
		# for room in self.rooms:
		# 	print(f">> ROOM `{room.name}` with status `{room.status}`")
		# 	print(f"\tX: `{room.coords[0]}`, Y: `{room.coords[1]}`")
		# for link in self.links:
		# 	print(f">> LINK from `{link.rooms[0]}` to `{link.rooms[1]}`")

	def read_input(self, lem_input):
		# lems = 0
		# rooms = []
		# links = []
		status_next = None
		for index, line in enumerate(lem_input):
			line = line.rstrip()
			if index == 0:
				self.lems = int(line)
				continue
			if line[0] is '#':
				if line[1] is '#':
					status_next = line[2:]
				continue
			if '-' in line:
				link1 = line[0:line.find('-')]
				link2 = line[line.find('-') + 1:]
				self.links.append(components.link.Link(link1, link2, self.rooms))
			else:
				params = line.split()
				if (len(params) < 3):
					print(f"Error in parsing. Invalid room : `{line}`")
					exit()
				coords = {'x': int(params[1]), 'y':int(params[2])}
				if (coords['x'] > self.bounds['x']): self.bounds['x'] = coords['x']
				if (coords['y'] > self.bounds['y']): self.bounds['y'] = coords['y']
				self.rooms.append(components.room.Room(params[0], coords, status_next, self.window))
				status_next = None
		for room in self.rooms:
			room.set_bounds(self.bounds)

	def elements(self, window):
		texts = []
		quads = []
		links = []
		for line in self.lem_input:
			print(line)
		context = ui.text.Context(window)
		texts.append(context.title('lem_in'))
		texts.append(pyg.text.Label('Bonjour toi'))
		for room in self.rooms:
			quads.append(room.vertices())
		for link in self.links:
			links.append(link.vertices())
		return {'texts': texts, 'quads': quads, 'links': links}
