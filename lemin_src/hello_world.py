# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hello_world.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/17 14:05:49 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/18 15:35:00 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyglet
import app
import sys

window = pyglet.window.Window()

app_instance = app.App(sys.stdin, window)
all_elements = app_instance.elements(window=window)


@window.event
def on_draw():
	window.clear()
	for text in all_elements['texts']:
		text.draw()
	for quad in all_elements['quads']:
		quad.draw(pyglet.gl.GL_QUADS)
	for link in all_elements['links']:
		link.draw(pyglet.gl.GL_LINES)

pyglet.app.run()
