# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    room.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/18 11:30:17 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/18 15:39:54 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyglet


class Room:
	name = ""
	type = None
	status = None
	coords = None
	bounds = {'x': 100, 'y': 100}
	window = None

	def __init__(self, name, coords, status, window):
		self.name = name
		self.status = status
		self.window = window
		self.coords = coords
	
	def set_bounds(self, bounds):
		self.bounds = bounds
		self.coords['x'] = int(self.coords['x'] / self.bounds['x'] * (self.window.width - 40))
		self.coords['y'] = int(self.coords['y'] / self.bounds['y'] * (self.window.height - 40))
	
	def vertices(self):
		# print(f"This room will be placed at coords {x}x{y}")
		YELLOW = (255, 255, 0)
		QUAD_VERT = 4
		QUAD_SIZE = 20
		first = (self.coords['x'], self.coords['y'])
		second = (self.coords['x'], self.coords['y'] + QUAD_SIZE)
		third = (self.coords['x'] + QUAD_SIZE, self.coords['y'] + QUAD_SIZE)
		forth = (self.coords['x'] + QUAD_SIZE, self.coords['y'])
		vertices = ('v2i', (*first, *second, *third, *forth))
		colors = ('c3B', YELLOW * QUAD_VERT)
		vertex_list = pyglet.graphics.vertex_list(QUAD_VERT, vertices, colors)
		return vertex_list
