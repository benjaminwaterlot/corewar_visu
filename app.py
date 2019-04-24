import arcade
# import draw.canvas
from draw import canvas
from helpers import fps_logger
from game_map import generate_map
import colors
from parser import parse_next, parse_start


class MyGame(arcade.Window):
	MARGIN = 20
	SCREEN_WIDTH = 2560
	SCREEN_HEIGHT = 1440
	SCREEN_TITLE = "Corewar"
	frame = 0

	def __init__(self):
		super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT,
		                 self.SCREEN_TITLE)
		arcade.set_background_color(colors.BROWN)
		self.map_sprites = None

		# self.set_fullscreen()
		width, height = self.get_size()
		self.set_viewport(0, width, 0, height)

	def setup(self):
		# next_cycle = parse_next()
		start_infos = parse_start()
		self.map_sprites = generate_map(self)

	def on_draw(self):
		arcade.start_render()
		canvas.draw(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
		self.map_sprites.draw()

	def on_update(self, delta_time):
		fps_logger(self, delta_time)


def main():
	game = MyGame()
	game.setup()
	arcade.run()


if __name__ == "__main__":
	main()
