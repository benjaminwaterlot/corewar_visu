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
        arcade.load_texture(
            f"resources/pokemons/0/tile{format(ref, '03d')}.png")
        for ref in [3, 4, 5, 79, 80]
    ],
    'pokemon':
    "resources/big_pokemons/dracofeu_big.png",
    'color':
    colors.YELLOW
},
             {
                 'pokemons': [
                     arcade.load_texture(
                         f"resources/pokemons/1/tile{format(ref, '03d')}.png")
                     for ref in [0, 1, 2, 9, 10]
                 ],
                 'pokemon':
                 "resources/big_pokemons/florizarre_big.png",
                 'color':
                 arcade.color.GREEN_YELLOW
             }]
