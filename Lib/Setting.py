from pygame.math import Vector2

# screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
TILE_SIZE = 64

# dialogue box
FONT_NAME = "../Font/FVF_Fernando_08.ttf"
FONT_SIZE = 12
DIALOGUE = "../Graphics/Dialog/Dialogue2.png"
DIALOGUE_WIDTH = SCREEN_WIDTH - 60
DIALOGUE_HEIGHT = 160
DIALOGUE_CENTER_X = 30
DIALOGUE_CENTER_Y = SCREEN_HEIGHT - (DIALOGUE_HEIGHT) - 15

LAYERS = {
    'water': 0,
    'ground': 1,
    'soil': 2,
    'soil water': 3,
    'rain floor': 4,
    'house bottom': 5,
    'ground plant': 6,
    'main': 7,
    'house top': 8,
    'fruit': 9,
    'rain drops': 10
}
NPC_Position = {
    "Jon": (512, 427),
    "Dam": (695, 352),
    "Junie": (1059, 582)
}
