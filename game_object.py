# game_object.py
import pygame
from constants import DEFAULT_IMAGE_SIZE


class GameObject:
    def __init__(self, image_path, x, y, screen):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
