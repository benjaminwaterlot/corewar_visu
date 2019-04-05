# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    text.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/17 14:20:16 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/17 15:49:12 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyglet as pyg


class Context:
	window = None

	def __init__(self, window):
		self.window = window

	def title(self, text):
		params = {
			'color': (209, 200, 10, 255),
			'font_name': 'Operator Mono',
			'font_size': 14,
			'x': 10,
			'y': self.window.height - 10,
			'anchor_x': 'left',
			'anchor_y': 'top',
		}
		return pyg.text.Label(text, **params)
