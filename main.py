# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys

import pygame

pygame.init()

GAME_TITLE = 'Space Invaders'
RESOURCE_DIR = 'resources'
SPRITE_DIR = os.path.join(RESOURCE_DIR, 'sprite')
BACKGROUND_DIR = os.path.join(RESOURCE_DIR, 'background')
GAME_ICON = os.path.join(SPRITE_DIR, 'alien1-arms-down.png')
DEFAULT_IMAGE_SIZE = (96, 96)
DEFAULT_DX = 5
DEFAULT_DY = 5
QUIT_TEXT = 'Press ESC to quit'
DEFAULT_FONT = pygame.font.SysFont(None, 32)
DEFAULT_BACKGROUND = pygame.image.load(os.path.join(BACKGROUND_DIR, 'nebula-and-stars.jpg'))


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(GAME_TITLE)
pygame.display.set_icon(pygame.image.load(GAME_ICON))
pygame.key.set_repeat(0, 150)

# Player Setup
player_image = pygame.image.load(os.path.join(SPRITE_DIR, 'player-ship.png'))
player_image = pygame.transform.scale(player_image, DEFAULT_IMAGE_SIZE)
player_x = 370
player_dx = 0
player_y = 480
player_dy = 0

# Laser beam:
# small white rectangle with gradient sides (eventually)
# Gradients are difficult, so start with 2-3 colors


def terminate():
    pygame.quit()
    sys.exit()


def player_update(x_pos, y_pos):
    screen.blit(player_image, (x_pos, y_pos))


def player_move_x(direction: int):
    global player_x
    player_x = player_x + (direction * DEFAULT_DX)


def player_move_y(direction: int):
    global player_y
    player_y = player_y + (direction * DEFAULT_DY)


def check_player_boundary():
    global player_y, player_x, player_image
    if player_x < 0:
        player_x = 0
    if player_x > screen.get_width() - player_image.get_width():
        player_x = screen.get_width() - player_image.get_width()

    if player_y < screen.get_height() - screen.get_height() // 3:
        player_y = screen.get_height() - screen.get_height() // 3
    if player_y > screen.get_height() - player_image.get_height():
        player_y = screen.get_height() - player_image.get_height()


def process_event(e):
    global player_y, player_x, running, player_dx, player_dy

    if e.type == pygame.QUIT:
        running = False
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_ESCAPE:
            running = False
        if e.key == pygame.K_LEFT:
            player_dx = -DEFAULT_DX
        if e.key == pygame.K_RIGHT:
            player_dx = DEFAULT_DX
        if e.key == pygame.K_UP:
            player_dy = -DEFAULT_DY
        if e.key == pygame.K_DOWN:
            player_dy = DEFAULT_DY
    if e.type == pygame.KEYUP:
        if e.key in [pygame.K_RIGHT, pygame.K_LEFT]:
            player_dx = 0
        if e.key in [pygame.K_UP, pygame.K_DOWN]:
            player_dy = 0


def check_collision():
    # Check to see if the ship has collided with anything
    pass


def check_bullet():
    # Check to see if bullet hit anything
    pass


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(DEFAULT_BACKGROUND, (0,0))
    for event in pygame.event.get():
        process_event(event)

    directions_text = DEFAULT_FONT.render("Use arrow keys to move. Press ESC to quit.", True, (255, 255, 255))
    directions_text_rect = directions_text.get_rect(center=(screen.get_width() / 2, 50))
    screen.blit(directions_text, directions_text_rect)

    player_x += player_dx
    player_y += player_dy
    check_player_boundary()
    player_update(player_x, player_y)
    pygame.display.update()

terminate()
