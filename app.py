import arcade
# import draw.canvas
from draw import canvas
from helpers import fps_logger
from game_map import generate_map
import colors
import const
from parser import parse_next, parse_start
from textures import ENERGY, POKEMON, EMPTY


class MyGame(arcade.Window):
	SCREEN_WIDTH = const.SCREEN_WIDTH
	SCREEN_HEIGHT = const.SCREEN_HEIGHT
	SCREEN_TITLE = "Corewar"
	frame = 0

	def __init__(self):
		super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT,
		                 self.SCREEN_TITLE)
		arcade.set_background_color(colors.BROWN)
		self.map_sprites = None
		self.cycle = "0"

		width, height = self.get_size()
		self.set_viewport(0, width, 0, height)

	def setup(self):
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

		print((updates))
		for update in updates:
			update = update.split()
			update_type = update[0]

			if update_type == 'C':
				self.cycle = update[1]

			elif update_type == 'M':
				location = int(update[1])
				champion = int(update[2])

				self.map_owners[location] = champion
				champion_on_case = self.map_owners[location]
				if champion_on_case == None:
					raise ValueError(
					    f"ERROR in cycle {self.cycle}: CHAMPION's TEXTURE IS NONETYPE, at case {location}"
					)
				self.map_sprites[location].set_texture(champion_on_case)

			elif update_type == 'P':
				if (not update[2].isdigit()):
					raise ValueError(
					    f"This update is not correct ! >> {update}")
				process_id = int(update[1])
				process_destination = int(update[2])
				process_champion = int(update[3])

				if process_id > len(self.processes):
					pokemon = POKEMON.salameche if process_champion is 1 else POKEMON.bulbizarre
					self.processes.append({
					    'champion': process_champion,
					    'location': process_destination,
					    'pokemon': pokemon
					})
					self.map_sprites[process_destination].set_texture(pokemon)
				else:
					process = self.processes[process_id - 1]
					process_location = process['location']
					# if self.map_owners[process_location] == None:
					# 	raise ValueError(
					# 	    f"ERROR in cycle {self.cycle}: PROCESS's DEPARTURE LOCATION's TEXTURE IS NONETYPE, at case {process_location}, values around being : {[self.map_owners[process_location + i] for i in range(-20, 40)]}"
					# 	)

					if self.map_owners[process_location]:
						self.map_sprites[process_location].set_texture(
						    self.map_owners[process_location])

					# if process['pokemon'] == None:
					# 	raise ValueError(
					# 	    f"ERROR in cycle {self.cycle}: PROCESS's POKEMON TEXTURE IS NONETYPE, at case {process_destination}"
					# 	)
					process['location'] = process_destination
					if process['pokemon']:
						self.map_sprites[process_destination].set_texture(
						    process['pokemon'])

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
