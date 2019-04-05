import arcade
import draw.canvas
import sprites
import helpers.map

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440 - 36
SCREEN_TITLE = "Corewar"


class MyGame(arcade.Window):
	string_input = ""
	frame = 0

	def __init__(self, width, height, title):
		super().__init__(width, height, title)

		arcade.set_background_color((62, 57, 57))
		self.pokemons_list = None

		# If you have sprite lists, you should create them here,
		# and set them to None

	def setup(self):
		self.pokemons_list = arcade.SpriteList()
		POKEGRID_X = 80
		POKEMON_SIZE = 24
		game_map = helpers.map.generate_map()

		for (index, value) in enumerate(game_map):
			center_x = 40 + index * POKEMON_SIZE % (POKEGRID_X * POKEMON_SIZE)
			center_y = SCREEN_HEIGHT - 200 - int(
			    index / POKEGRID_X) * POKEMON_SIZE

			empty = sprites.empty(center_x, center_y)
			self.pokemons_list.append(empty)

			if value is not None:
				name = "salameche" if value == 1 else "bulbizarre"
				pokemon = sprites.pokemon(name, center_x, center_y)
				self.pokemons_list.append(pokemon)

	def on_draw(self):
		arcade.start_render()
		draw.canvas.draw(SCREEN_WIDTH, SCREEN_HEIGHT)
		self.pokemons_list.draw()

	def on_update(self, delta_time):
		self.frame += 1
		if (not self.frame % 30):
			print(f"FPS: {round(1 / delta_time)}")


def main():
	""" Main method """
	game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
	game.setup()
	arcade.run()


if __name__ == "__main__":
	main()
