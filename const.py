import arcade
import colors

# GENERAL
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440
MARGIN = 20

# PANEL
PANEL_WIDTH = 440

# ARENA
ARENA_CENTER = (SCREEN_WIDTH - PANEL_WIDTH) / 2

# GRID
MAP_SIZE = 4096
GRID_X = 85
POKEMON_SIZE = 24

# SETTINGS
SPEED = 2

CHAMPIONS = [{
	'pokemons': [
		arcade.load_texture(f"resources/fire/tile{format(ref, '03d')}.png")
		for ref in [3, 4, 5, 79, 80, 59, 60, 130, 140, 160, 161, 162]
	],
	'pokemon': "resources/fire/big.png",
	'energy': "resources/fire/energy.png",
	'live':
	arcade.load_texture("resources/fire/live.png"),
	'color':
	colors.YELLOW
},
{
	'pokemons': [
	arcade.load_texture(
	f"resources/plant/tile{format(ref, '03d')}.png")
	for ref in [0, 1, 2, 9, 10, 126, 157, 159]
	],
	'pokemon': "resources/plant/big.png",
	'energy': "resources/plant/energy.png",
	'live':
	arcade.load_texture("resources/plant/live.png"),
	'color':
	arcade.color.GREEN_YELLOW
},
{
	'pokemons': [
	arcade.load_texture(
	f"resources/water/tile{format(ref, '03d')}.png")
	for ref in [6, 7, 8, 88, 89, 119, 120, 134, 135]
	],
	'pokemon': "resources/water/big.png",
	'energy': "resources/water/energy.png",
	'live':
	arcade.load_texture("resources/water/live.png"),
	'color':
	arcade.color.BLUE_SAPPHIRE
},
{
'pokemons': [
	arcade.load_texture(
	f"resources/electricity/tile{format(ref, '03d')}.png")
	for ref in [24, 26, 177, 185, 187, 213, 247, 322, 323]
	],
	'pokemon': "resources/electricity/big.png",
	'energy': "resources/electricity/energy.png",
	'live':
	arcade.load_texture("resources/electricity/live.png"),
	'color':
	arcade.color.YELLOW
}]
