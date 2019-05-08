import arcade
import colors
import const
import sprites
import textures
from objects import Champion


def get_champion_infos(game, champion: Champion, winner: Champion):
	is_winner = winner.id == champion.id

	default_y = const.SCREEN_HEIGHT / 2
	# y = default_y + 100 if is_winner else default_y
	x = const.SCREEN_WIDTH / 2 - 150 * len(game.champions) + champion.id * 300
	scale = 1 if is_winner else .5

	return arcade.Sprite(
	    champion.pokemon, scale=scale, center_x=x, center_y=default_y)


class EndCanvas():
	def __init__(self, game, winner_ref, winner: Champion):
		self.winner_ref = winner_ref
		self.winner = winner
		self.game = game

		self.pokemons = [
		    get_poke_sprite(game, champ, winner) for champ in game.champions
		]

	def draw_canvas(self):
		arcade.draw_text(
		    text="The winner is",
		    align="center",
		    start_x=const.SCREEN_WIDTH / 2 - 1200 / 2,
		    start_y=const.SCREEN_HEIGHT - 380,
		    color=self.winner.color,
		    font_name="Pokemon Solid",
		    width=1200,
		    font_size=36),

		arcade.draw_text(
		    text=self.winner.name,
		    align="center",
		    start_x=const.SCREEN_WIDTH / 2 - 1200 / 2,
		    start_y=const.SCREEN_HEIGHT - 500,
		    color=self.winner.color,
		    font_name="Pokemon Solid",
		    width=1200,
		    font_size=64),

		for poke in self.pokemons:
			poke.draw()
