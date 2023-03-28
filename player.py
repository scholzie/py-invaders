# player.py
from game_object import GameObject
from constants import PLAYER_DX, PLAYER_DY, PLAYER_LASER_COLOR, PLAYER_LASER_SIZE, PLAYER_SIZE
import pygame
from projectile import Laser


class Player(GameObject):
    def __init__(self, image_path, x, y, screen):
        image = pygame.image.load(image_path)
        super().__init__(image, x, y, screen)
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.dx = PLAYER_DX
        self.dy = PLAYER_DY

    def move_x(self, direction: int, dx: int = PLAYER_DX):
        self.x += direction * dx

    def move_y(self, direction: int, dy: int = PLAYER_DY):
        self.y += direction * dy

    def check_boundary(self):
        if self.x < 0:
            self.x = 0
        if self.x > self.screen.get_width() - self.image.get_width():
            self.x = self.screen.get_width() - self.image.get_width()

        if self.y < self.screen.get_height() - self.screen.get_height() // 3:
            self.y = self.screen.get_height() - self.screen.get_height() // 3
        if self.y > self.screen.get_height() - self.image.get_height():
            self.y = self.screen.get_height() - self.image.get_height()

    def fire_laser(self, laser_image=None):
        laser_x = self.x + self.image.get_width() // 2 - PLAYER_LASER_SIZE[0] // 2
        laser_y = self.y - PLAYER_LASER_SIZE[1]
        if laser_image:
            return Laser.from_image(laser_image,
                                    laser_x,
                                    laser_y,
                                    self.screen)

        return Laser.from_rect(PLAYER_LASER_COLOR,
                               PLAYER_LASER_SIZE[0],
                               PLAYER_LASER_SIZE[1],
                               laser_x,
                               laser_y,
                               self.screen)
