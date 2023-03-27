# constants.py
import os
import pygame

# Constants
GAME_TITLE = 'Space Invaders'
RESOURCE_DIR = 'resources'
SPRITE_DIR = os.path.join(RESOURCE_DIR, 'sprite')
BACKGROUND_DIR = os.path.join(RESOURCE_DIR, 'background')
GAME_ICON = os.path.join(SPRITE_DIR, 'alien1-arms-down.png')
ENEMY_1_IMAGE = os.path.join(SPRITE_DIR, 'alien1-arms-down.png')
ENEMY_2_IMAGE = os.path.join(SPRITE_DIR, 'alien1-arms-up.png')
ENEMY_SIZE = (40, 40)
ENEMY_ROWS = 5
ENEMY_COLS = 11
PLAYER_SIZE = (96, 96)
PLAYER_DX = 5
PLAYER_DY = 5
QUIT_TEXT = 'Press ESC to quit'
DEFAULT_BACKGROUND = pygame.image.load(os.path.join(BACKGROUND_DIR, 'nebula-and-stars.jpg'))
