import arcade
import colors
import const


def draw(game):
	arcade.draw_text(
	    text="corewar",
	    align="center",
	    start_x=const.SCREEN_WIDTH / 2 - 200 / 2,
	    start_y=const.SCREEN_HEIGHT - 80,
	    color=colors.YELLOW,
	    font_name="Pokemon Solid",
	    width=300,
	    font_size=42)

	arcade.draw_rectangle_filled(
	    center_x=const.ARENA_CENTER,
	    center_y=(const.SCREEN_HEIGHT - 90) / 2,
	    height=const.SCREEN_HEIGHT - 220,
	    width=const.SCREEN_WIDTH - 480,
	    color=(0, 0, 0, 70))

	arcade.draw_text(
	    text=game.cycle,
	    align="center",
	    start_x=const.SCREEN_WIDTH / 2 - 200 / 2,
	    start_y=const.SCREEN_HEIGHT - 120,
	    color=colors.WHITE,
	    font_name="Pokemon Solid",
	    width=300,
	    font_size=18)
