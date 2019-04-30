import arcade
# import draw.canvas
from draw import canvas
from helpers import fps_logger
from game_map import generate_map
import colors
import const
from parser import parse_next, parse_start
from textures import ENERGY, POKEMON, EMPTY, get_loaded_textures

from threading import Thread

# import random
# import sys
# import time

# class Afficheur(Thread):
# 	"""Thread chargé simplement d'afficher une lettre dans la console."""

# 	def __init__(self, lettre):
# 		Thread.__init__(self)
# 		self.lettre = lettre

# 	def run(self):
# 		"""Code à exécuter pendant l'exécution du thread."""
# 		i = 0
# 		while i < 20:
# 			sys.stdout.write(self.lettre)
# 			sys.stdout.flush()
# 			attente = 0.2
# 			attente += random.randint(1, 60) / 100
# 			time.sleep(attente)
# 			i += 1


class MyGame(arcade.Window):
	SCREEN_WIDTH = const.SCREEN_WIDTH
	SCREEN_HEIGHT = const.SCREEN_HEIGHT
	SCREEN_TITLE = "Corewar"
	frame = 0
	M_count = 0
	P_count = 0

	def __init__(self):
		super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT,
		                 self.SCREEN_TITLE)
		arcade.set_background_color(colors.BROWN)
		self.map_sprites = None
		self.cycle = "0"

		width, height = self.get_size()
		self.set_viewport(0, width, 0, height)

	def setup(self):
		self.textures = get_loaded_textures()
		self.start_infos = parse_start()
		self.map_owners = [
		    int(case) if case.isdigit() else None
		    for case in self.start_infos['starting_map']
		]
		self.processes = self.start_infos['processes']
		self.map_sprites = generate_map(self)

	def on_update(self, delta_time):
		fps_logger(self, delta_time)

		obsolete_sprites = []
		updates = parse_next(const.SPEED)

		# print(updates)
		for raw_update in updates:
			update = raw_update.split()
			update_type = update[0]

			if update_type == 'C':
				self.cycle = update[1]

			elif update_type == 'M':
				self.M_count += 1
				location = int(update[1])
				champion = int(update[2])

				self.map_owners[location] = champion
				champion_on_case = self.map_owners[location]
				if champion_on_case == None:
					raise ValueError(
					    f"ERROR in cycle {self.cycle}: CHAMPION's TEXTURE IS NONETYPE, at case {location}"
					)
				for index in range(location, location + 4):
					self.map_sprites[index % const.MAP_SIZE].set_texture(
					    champion_on_case)
					pass

			elif update_type == 'P':
				self.P_count += 1
				# if (not update[2].isdigit()):
				# 	raise ValueError(
				# 	    f"This update is not correct ! >> {raw_update}")
				process_id = int(update[1])
				process_destination = None if update[2] == 'x' else int(
				    update[2])
				process_champion = int(
				    update[3]) if process_destination else None

				if process_id > len(self.processes):
					pokemon = EMPTY
					if process_champion == 1:
						pokemon = POKEMON.salameche
					elif process_champion == 2:
						pokemon = POKEMON.bulbizarre
					self.processes.append({
					    'champion': process_champion,
					    'location': process_destination,
					    'pokemon': pokemon
					})
					self.map_sprites[process_destination].set_texture(pokemon)
				else:
					process = self.processes[process_id - 1]
					process_location = process['location']
					process_pokemon = process['pokemon']

					if self.map_owners[process_location]:
						self.map_sprites[process_location].set_texture(
						    self.map_owners[process_location])
						pass

					process['location'] = process_destination
					if process_pokemon:
						self.map_sprites[process_destination].set_texture(
						    process_pokemon)
						pass

	def on_draw(self):
		arcade.start_render()
		canvas.draw(self)
		self.map_sprites.draw()


def main():
	game = MyGame()
	game.setup()
	arcade.run()


if __name__ == "__main__":
	main()
