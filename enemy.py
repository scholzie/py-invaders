# enemy.py
from game_object import GameObject
from constants import ENEMY_SIZE, ENEMY_1_IMAGE, ENEMY_2_IMAGE
import pygame


class Enemy(GameObject):
    def __init__(self, image_path, x, y, screen):
        super().__init__(image_path, x, y, screen)
        self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

    def move(self):
        pass

    def update(self):
        self.move()


class EnemyType1(Enemy):
    def __init__(self, x, y, screen):
        super().__init__(ENEMY_1_IMAGE, x, y, screen)

    def move(self):
        super().move()

    def update(self):
        super().update()


class EnemyType2(Enemy):
    def __init__(self, x, y, screen):
        super().__init__(ENEMY_2_IMAGE, x, y, screen)

    def move(self):
        super().move()

    def update(self):
        super().update()
