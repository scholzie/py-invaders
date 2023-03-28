# main.py
import sys
from game import Game
import pygame


def terminate():
    pygame.quit()
    sys.exit()


def main():
    game = Game()
    game.run()

    terminate()


if __name__ == '__main__':
    main()
