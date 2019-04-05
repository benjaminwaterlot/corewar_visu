import arcade


def pokemon(name, x, y):
	return arcade.Sprite(
	    filename=f"resources/{name}.png", scale=.75, center_x=x, center_y=y)


def empty(x, y):
	return arcade.Sprite(
	    filename=f"resources/empty.png", scale=.6, center_x=x, center_y=y)
