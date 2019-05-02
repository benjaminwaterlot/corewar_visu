import arcade
from draw import canvas
from helpers import fps_logger
import helpers
import game_map
import colors
import const
from parser import parse_next, parse_start
import textures
import sprites

from threading import Thread


class MyGame(arcade.Window):
	SCREEN_WIDTH = const.SCREEN_WIDTH
	SCREEN_HEIGHT = const.SCREEN_HEIGHT
	SCREEN_TITLE = "Corewar"
	frame = 0

	def __init__(self):
		super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT,
		                 self.SCREEN_TITLE)
		arcade.set_background_color(colors.BROWN)
		self.terrain_sprites = None
		self.cycle = "0"
		self.process_count = [1, 1, 1, 1]

		width, height = self.get_size()
		self.set_viewport(0, width, 0, height)

	def setup(self):
		self.terrain_textures = textures.load_terrain_textures()
		self.pokemon_textures = textures.load_pokemon_textures()
		self.big_pokemon_textures = textures.load_big_pokemon_textures()

		(self.starting_map, self.champions, self.pokemons) = parse_start()
		self.canvas = canvas.Canvas(self)
		self.pokemons_sprites = game_map.generate_process_sprites(self)

		self.terrain_owners = [
		    int(case) if case.isdigit() else None for case in self.starting_map
		]
		self.terrain_sprites = game_map.generate_map(self)

	def on_update(self, delta_time):
		self.frame += 1
		if (not self.frame % 30):
			fps_logger(self, delta_time)
			print(self.process_count)

		updates = parse_next(const.SPEED)

		for raw_update in updates:
			update = raw_update.split()
			update_type = update[0]

			if update_type == 'C':
				self.cycle = update[1]

			elif update_type == 'M':
				location = int(update[1])
				champion = int(update[2])

				if self.terrain_owners[location] == champion:
					break

				self.terrain_owners[location] = champion
				champion_on_case = self.terrain_owners[location]
				if champion_on_case == None:
					raise ValueError(
					    f"ERROR in cycle {self.cycle}: CHAMPION's TEXTURE IS NONETYPE, at case {location}"
					)
				for index in range(location, location + 4):
					self.terrain_sprites[index % const.MAP_SIZE].set_texture(
					    champion_on_case)
					pass

			elif update_type == 'P':
				process_id = int(update[1])
				process_destination = None if update[2] == 'x' else int(
				    update[2])
				process_champion = int(
				    update[3]) if process_destination else None

				# Si ce n'est pas une mort de process
				if process_destination:
					# Si le process vient de spawn
					if process_id > len(self.pokemons_sprites):
						texture = self.pokemon_textures[process_champion]
						self.pokemons_sprites.append(
						    sprites.pokemon(texture, process_destination,
						                    process_champion - 1))
						self.process_count[process_champion - 1] += 1
					# Si le process existait et se déplace
					else:
						if process_destination is None:
							break
						(x, y) = helpers.get_grid_coords(process_destination)
						self.pokemons_sprites[process_id - 1].center_x = x
						self.pokemons_sprites[process_id - 1].center_y = y
				else:
					if process_id <= len(self.pokemons_sprites):
						self.pokemons_sprites[process_id - 1].alpha = 0

	def on_key_press(self, key, modifiers):
		if key == arcade.key.DOWN or key == arcade.key.UP:
			new_speed = const.SPEED
			if key == arcade.key.DOWN:
				new_speed -= 1
			elif key == arcade.key.UP:
				new_speed += 1
			if new_speed < 1: new_speed = 1
			if new_speed > 10: new_speed = 10

			const.SPEED = new_speed

	def on_draw(self):
		arcade.start_render()
		self.canvas.draw_canvas()
		self.terrain_sprites.draw()
		self.pokemons_sprites.draw()


def main():
	game = MyGame()
	game.setup()
	arcade.run()


if __name__ == "__main__":
	main()
