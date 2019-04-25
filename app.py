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

		for update in updates:
			update = update.split()
			if update[0] == 'C':
				self.cycle = update[1]

			if update[0] == 'M':
				location = int(update[1])
				champion = int(update[2])

				self.map_owners[location] = champion
				obsolete_sprites.append({
				    'location': location,
				    'type': 'energy'
				})

			if update[0] == 'P':
				process_id = int(update[1])
				process_location = int(update[2])
				process_champion = int(update[3])
				if process_id > len(self.processes):
					pokemon = POKEMON.salameche if process_champion is 1 else POKEMON.bulbizarre
					self.processes.append({
					    'champion': process_champion,
					    'location': process_location,
					    'pokemon': pokemon
					})
					self.map_sprites[process_location].set_texture(pokemon)
				else:
					process = self.processes[process_id - 1]
					# obsolete_sprites.append({
					#     'location': process['location'],
					#     'type': 'energy'
					# })
					self.map_sprites[process['location']].set_texture(
					    self.map_owners[process['location']])
					process['location'] = process_location
					self.map_sprites[process_location].set_texture(
					    process['pokemon'])

		for sprite in obsolete_sprites:
			if sprite['type'] == 'energy':
				update_location = sprite['location']
				champion_on_case = self.map_owners[update_location]
				if champion_on_case == 'x':
					return
				self.map_sprites[update_location].set_texture(champion_on_case)

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
