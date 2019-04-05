# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    link.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/18 11:31:01 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/18 15:41:31 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyglet


class Link:
	rooms = None
	first = None
	second = None
	def __init__(self, first, second, all_rooms):
		for room in all_rooms:
			if room.name == first:
				self.first = room
			if room.name == second:
				self.second = room
			if self.first and self.second:
				break
		print(f"This link is tied to {self.first.name} and {self.second.name}")
	
	def vertices(self):
		start_x = self.first.coords['x']
		start_y = self.first.coords['y']
		end_x = self.second.coords['x']
		end_y = self.second.coords['y']

		COLOR = (0, 255, 0)
		vertices = ('v2i', (start_x, start_y, end_x, end_y, start_x + 5, start_y + 5, end_x + 5, end_y + 5))
		colors = ('c3B', COLOR * 4)
		vertex_list = pyglet.graphics.vertex_list(4, vertices, colors)
		return vertex_list


	# def __init__(self, name, coords, status, window):
	# 	self.name = name
	# 	self.status = status
	# 	self.coords = coords
	# 	self.window = window
	
	# def set_bounds(self, bounds):
	# 	self.bounds = bounds
	
	# def vertices(self):
	# 	x = int(self.coords[0] / self.bounds['x'] * (self.window.width - 40))
	# 	y = int(self.coords[1] / self.bounds['y'] * (self.window.height - 40))
	# 	print(f"This room will be placed at coords {x}x{y}")

	# 	YELLOW = (255, 255, 0)
	# 	QUAD_VERT = 4
	# 	QUAD_SIZE = 20
	# 	first = (x, y)
	# 	second = (x, y + QUAD_SIZE)
	# 	third = (x + QUAD_SIZE, y + QUAD_SIZE)
	# 	forth = (x + QUAD_SIZE, y)
	# 	vertices = ('v2i', (*first, *second, *third, *forth))
	# 	colors = ('c3B', YELLOW * QUAD_VERT)
	# 	vertex_list = pyglet.graphics.vertex_list(QUAD_VERT, vertices, colors)
	# 	return vertex_list

