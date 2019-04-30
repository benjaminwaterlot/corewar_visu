import arcade
import colors
import const


def draw(game):
	for draw in shapes:
		draw(game)


cycle_label_y = const.SCREEN_HEIGHT - 120
speed_label_y = const.SCREEN_HEIGHT - 50
speed_label_x = 0

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