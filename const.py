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
    'pokemon': "resources/big_pokemons/dracofeu_big.png",
    'color': colors.YELLOW
},
             {
                 'pokemon': "resources/big_pokemons/florizarre_big.png",
                 'color': arcade.color.GREEN_YELLOW
             }]
