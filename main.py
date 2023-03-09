# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

import pygame

GAME_TITLE = 'Space Invaders'
GAME_ICON = os.path.join('resources', 'pixel-alien.png')
DEFAULT_IMAGE_SIZE = (96, 96)
DEFAULT_DX = 20
DEFAULT_DY = 20
QUIT_TEXT = 'Press ESC to quit'

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(GAME_TITLE)
pygame.display.set_icon(pygame.image.load(GAME_ICON))
pygame.key.set_repeat(50, 50)

# Player Setup
player_image = pygame.image.load(os.path.join('resources', 'player-ship.png'))
player_image = pygame.transform.scale(player_image, DEFAULT_IMAGE_SIZE)
player_x = 370
player_x_moving = False
player_y = 480
player_y_moving = False


def player_update(x_pos, y_pos):
    check_boundary(player_image)
    screen.blit(player_image, (x_pos, y_pos))


def player_move_x(direction: int):
    global player_x
    player_x = player_x + (direction * DEFAULT_DX)


def player_move_y(direction: int):
    global player_y
    player_y = player_y + (direction * DEFAULT_DY)


def check_boundary(player: pygame.Surface):
    global player_y, player_x
    if player_x < 0:
        player_x = 0
    if player_x > screen.get_width() - player.get_width():
        player_x = screen.get_width() - player.get_width()

    if player_y < screen.get_height() - screen.get_height() // 3:
        player_y = screen.get_height() - screen.get_height() // 3
    if player_y > screen.get_height() - player.get_height():
        player_y = screen.get_height() - player.get_height()


def process_event(e):
    global player_y, player_x, running, player_x_moving, player_y_moving

    if e.type == pygame.QUIT:
        running = False
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_ESCAPE:
            running = False
        if e.key == pygame.K_LEFT:
            player_move_x(-1)
        if e.key == pygame.K_RIGHT:
            player_move_x(1)
        if e.key == pygame.K_UP:
            player_move_y(-1)
        if e.key == pygame.K_DOWN:
            player_move_y(1)
    # if e.type == pygame.KEYUP:
    #     if e.key in [pygame.K_RIGHT, pygame.K_LEFT]:
    #         player_x_moving = None
    #     if e.key in [pygame.K_UP, pygame.K_DOWN]:
    #         player_y_moving = None


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        process_event(event)

    screen.fill((0, 0, 0))
    player_update(player_x, player_y)
    pygame.display.update()
