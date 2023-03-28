# projectile.py
import pygame
from pygame import Surface

from game_object import GameObject
from constants import PLAYER_LASER_SIZE, PLAYER_LASER_IMAGE


class Projectile(GameObject):
    def __init__(self, image: Surface, x, y, screen):
        super().__init__(image, x, y, screen)

    def move(self):
        pass

    def update(self):
        self.move()

    def out_of_bounds(self):
        return self.y < 0 or self.y > self.screen.get_height()


class Laser(Projectile):
    def __init__(self, image: Surface, x, y, screen):
        super().__init__(image, x, y, screen)
        self.image = pygame.transform.scale(self.image, PLAYER_LASER_SIZE)

    @classmethod
    def from_image(cls, image_path, x, y, screen):
        image = pygame.image.load(image_path)
        return cls(image, x, y, screen)

    @classmethod
    def from_rect(cls, color, width, height, x, y, screen):
        image = pygame.Surface((width, height))
        image.fill(color)
        return cls(image, x, y, screen)

    def move(self):
        super().move()

    def move_y(self, direction: int, dy: int = 10):
        self.y += direction * dy

    def update(self):
        super().update()

    def check_boundary(self):
        super().check_boundary()
