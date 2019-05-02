import arcade
import colors
import const
import sprites
import textures
from app import MyGame


def draw_champions(game:MyGame, canvas):
	champions = game.champions

	def draw_champ_title(champion, index):
		arcade.draw_text(
			text=champion.name,
			align="center",
			start_x=const.SCREEN_WIDTH - 320,
			start_y=const.SCREEN_HEIGHT - 200 - 310 * index,
			color=champion.color,
			font_name="Pokemon Solid",
			width=200,
			font_size=20) 
	
	def draw_champ_process_count(game, champion, index):
		arcade.draw_text(
			text=f"{str(game.process_count[champion.id])} processes",
			align="center",
			start_x=const.SCREEN_WIDTH - 320,
			start_y=const.SCREEN_HEIGHT - 430 - 310 * index,
			color=champion.color,
			font_name="Pokemon Solid",
			width=200,
			font_size=10) 
	
	def draw_pokemon(champion, index, poke_sprite):
		poke_sprite.draw()

	for index, champion in enumerate(champions):
		draw_champ_title(champion, index)
		draw_champ_process_count(game, champion, index)
		draw_pokemon(champion, index, canvas.big_poke_sprites[index])
	
class Canvas():
	def __init__(self, game:MyGame):
		self.game = game
		self.big_poke_textures = textures.load_big_pokemon_textures()
		self.big_poke_sprites = arcade.SpriteList()

		for index, champion in enumerate(self.game.champions):
			coords = (const.SCREEN_WIDTH - 250, const.SCREEN_HEIGHT - 300 - 300 * index)
			self.big_poke_sprites.append(sprites.Big_Pokemon(self.big_poke_textures[index], coords))

	def draw_canvas(self):
		draw_champions(self.game, self)

		shapes = [
			# MAIN TITLE
			lambda game: arcade.draw_text(
				text="corewar",
				align="center",
				start_x=const.SCREEN_WIDTH / 2 - 200 / 2,
				start_y=const.SCREEN_HEIGHT - 80,
				color=colors.YELLOW,
				font_name="Pokemon Solid",
				width=300,
				font_size=42),

			# CANVAS
			lambda game: arcade.draw_rectangle_filled(
				center_x=const.ARENA_CENTER,
				center_y=(const.SCREEN_HEIGHT - 90) / 2,
				height=const.SCREEN_HEIGHT - 220,
				width=const.SCREEN_WIDTH - 480,
				color=(0, 0, 0, 70)),

			# SPEED LABEL
			lambda game: arcade.draw_text(
				text=str(const.SPEED),
				align="center",
				start_x=speed_label_x,
				start_y=speed_label_y,
				color=colors.YELLOW,
				font_name="Pokemon Solid",
				width=150,
				font_size=12),

			lambda game: arcade.draw_text(
				text="cycles / frame",
				align="center",
				start_x=speed_label_x,
				start_y=speed_label_y - 20,
				color=colors.WHITE,
				font_name="Pokemon Solid",
				width=150,
				font_size=10),

			# CYCLE LABEL
			lambda game: arcade.draw_text(
				text=game.cycle,
				align="center",
				start_x=const.SCREEN_WIDTH / 2 - 200 / 2,
				start_y=cycle_label_y,
				color=colors.WHITE,
				font_name="Pokemon Solid",
				width=300,
				font_size=18),
		]

		for draw in shapes:
			draw(self.game)


cycle_label_y = const.SCREEN_HEIGHT - 120
speed_label_y = const.SCREEN_HEIGHT - 50
speed_label_x = 0
