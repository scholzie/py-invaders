# player.py
from game_object import GameObject
from constants import DEFAULT_DX, DEFAULT_DY


class Player(GameObject):
    def __init__(self, image_path, x, y, screen):
        super().__init__(image_path, x, y, screen)

    def move_x(self, direction: int, dx: int = DEFAULT_DX):
        self.x += direction * dx

    def move_y(self, direction: int, dy: int = DEFAULT_DY):
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
