import arcade


def draw(SCREEN_WIDTH, SCREEN_HEIGHT):
	arcade.draw_text(
	    text="corewar",
	    align="center",
	    start_x=SCREEN_WIDTH / 2 - 200 / 2,
	    start_y=SCREEN_HEIGHT - 40,
	    color=arcade.color.WHITE_SMOKE,
	    font_name="PressStart2P-Regular",
	    width=200,
	    font_size=12)

	arcade.draw_rectangle_filled(
	    center_x=(SCREEN_WIDTH - 200) / 2,
	    center_y=(SCREEN_HEIGHT - 80) / 2,
	    height=SCREEN_HEIGHT - 120,
	    width=SCREEN_WIDTH - 240,
	    color=(0, 0, 0, 70))
