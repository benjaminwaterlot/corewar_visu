import arcade
from draw import canvas
from helpers import fps_logger
from parser import parse_next, parse_start
import helpers
import game_map
import colors
import const
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

		self.cycle = "0"
		self.last_speed = 0
		self.process_count = [1, 1, 1, 1]
		self.last_live = [1, 0, 0, 0]

		width, height = self.get_size()
		self.set_viewport(0, width, 0, height)

	def setup(self):
		self.big_pokemon_textures = textures.load_big_pokemon_textures()

		# LIVE SPRITES TO DISPLAY
		self.live_sprites = arcade.SpriteList()

		(self.starting_map, self.champions, self.pokemons) = parse_start()

		self.canvas = canvas.Canvas(self)
		self.pokemons_sprites = game_map.generate_process_sprites(self)

		self.terrain_owners = [
		    int(case) if case.isdigit() else 0 for case in self.starting_map
		]

		# SET UP THE 4 TERRAIN SPRITE LISTS
		self.terrain_sprites = [arcade.SpriteList() for _ in self.champions]

		# FILL THEM
		for champion, sprite_list in enumerate(self.terrain_sprites):
			for location in range(0, 4096):
				(x, y) = helpers.get_grid_coords(location)
				sprite_list.append(sprites.Terrain(champion + 1, x, y, False))
		# ADAPT THEM TO THE STARTING MAP
		for idx, bit in enumerate(self.terrain_owners):
			if bit > 0:
				self.terrain_sprites[bit - 1][idx].alpha = 255

	def on_update(self, delta_time):
		self.frame += 1

		if (not self.frame % 30):
			fps_logger(self, delta_time)

		updates = parse_next(const.SPEED)

		self.last_live = helpers.update_lives(self.last_live)

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
					champ_ref = champion_on_case - 1
					case = index % const.MAP_SIZE
					for i, champion in enumerate(self.champions):
						self.terrain_sprites[i][
						    case].alpha = 255 if i == champ_ref else 0

			elif update_type == 'P':
				process_id = int(update[1])
				process_destination = None if update[2] == 'x' else int(
				    update[2])
				process_champion = int(
				    update[3]) - 1 if process_destination else None

				# Si ce n'est pas une mort de process
				if process_destination:

					# Si le process vient de spawn
					if process_id > len(self.pokemons_sprites):
						self.pokemons_sprites.append(
						    sprites.pokemon(
						        helpers.get_random_pokemon(process_champion),
						        process_destination, process_champion))
						self.process_count[process_champion] += 1

					# Si le process existait et se déplace
					else:
						if process_destination is None:
							break
						(x, y) = helpers.get_grid_coords(process_destination)
						self.pokemons_sprites[process_id - 1].center_x = x
						self.pokemons_sprites[process_id - 1].center_y = y

				# Si c'est une mort de process:
				else:
					if process_id <= len(self.pokemons_sprites):
						self.pokemons_sprites[process_id - 1].alpha = 0

			elif update_type == 'L':
				player = int(update[1])
				self.live_sprites.append(
				    sprites.Live(player, len(self.live_sprites)))
				if len(self.live_sprites) > 74:
					self.live_sprites[0].kill()
					self.live_sprites.move(0, 16)

			# Si la ligne n'est pas reconnue
			else:
				print(F"WHAT IS THIS UNPARSED THING ? {update}")

	def on_key_press(self, key, modifiers):
		print(key)
		if key in [arcade.key.SPACE, 48]:
			if const.SPEED > 0:
				self.last_speed = const.SPEED
				const.SPEED = 0
			else:
				const.SPEED = self.last_speed

		elif key in range(48, 57 + 1):
			value = key - 48
			const.SPEED = value

		elif key in range(65456, 65465 + 1):
			value = key - 65456
			const.SPEED = value

		elif key == arcade.key.DOWN or key == arcade.key.UP:
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
		self.live_sprites.draw()
		for terrain in self.terrain_sprites:
			terrain.draw()
		self.pokemons_sprites.draw()


def main():
	game = MyGame()
	game.setup()
	arcade.run()


if __name__ == "__main__":
	main()
