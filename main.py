# main.py
import random
import sys
from constants import *
from player import Player
from enemy import EnemyType1, EnemyType2

pygame.init()
pygame.font.init()
DEFAULT_FONT = pygame.font.SysFont(None, 32)


def terminate():
    pygame.quit()
    sys.exit()



def check_collision(obj1, obj2):
    obj1_rect = obj1.image.get_rect(topleft=(obj1.x, obj1.y))
    obj2_rect = obj2.image.get_rect(topleft=(obj2.x, obj2.y))
    return obj1_rect.colliderect(obj2_rect)


def main():
    # Screen Setup
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(GAME_TITLE)
    pygame.display.set_icon(pygame.image.load(GAME_ICON))

    # Player Setup
    player_image = PLAYER_IMAGE
    player = Player(player_image, 370, 480, screen)
    laser_image = PLAYER_LASER_IMAGE
    lasers = []


    # Game Loop
    running = True


    terminate()


if __name__ == '__main__':
    main()
