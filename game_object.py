# game_object.py
import pygame
from pygame import Surface


class GameObject:
    def __init__(self, image: Surface, x, y, screen):
        self.image = image
        self.x = x
        self.y = y
        self.screen = screen

    @classmethod
    def from_image(cls, image_path, x, y, screen):
        image = pygame.image.load(image_path)
        return cls(image, x, y, screen)

    @classmethod
    def from_rect(cls, color, width, height, x, y, screen):
        image = pygame.Surface((width, height))
        image.fill(color)
        return cls(image, x, y, screen)

    def check_boundary(self):
        pass

    def draw(self):
        self.check_boundary()
        self.screen.blit(self.image, (self.x, self.y))
