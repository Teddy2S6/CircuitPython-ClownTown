#!/usr/bin/env python3

# Created by: Teddy Sannan & Jack D'Angelo
# Created on: January 2019
# This constants file is CircuitPython Stage game

# CircuitPython screen size is 160x128 and sprites are 16x16
#!/usr/bin/env python3

# Created by: Teddy Sannan & Jack D'Angelo
# Created on: January 2019
# This constants file is CircuitPython Stage game

# CircuitPython screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_TOMATOS = 15
TOTAL_NUMBER_OF_PIES = 15
TOTAL_NUMBER_OF_BALLOONS = 15
CLOWN_SPEED = 2
TOMATO_SPEED = 2
PIE_SPEED = 4
BALLOON_SPEED = 3
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60

MT_GAME_STUDIO_PALETTE = (b'\xf8\x1f\x00\x00\xcey\x00\xff\xf8\x1f\xff\x19\xfc\xe0\xfd\xe0'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

SCORE_PALETTE = (b'\xf8\x1f\x00\x00\xcey\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}
