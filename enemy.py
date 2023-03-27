# enemy.py
from game_object import GameObject
from constants import PLAYER_DX, PLAYER_DY, ENEMY_1_IMAGE, ENEMY_2_IMAGE


class Enemy(GameObject):
    def __init__(self, image_path, x, y, screen, dx=PLAYER_DX, dy=PLAYER_DY):
        super().__init__(image_path, x, y, screen)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def update(self):
        self.move()


class EnemyType1(Enemy):
    def __init__(self, x, y, screen, dx=PLAYER_DX, dy=PLAYER_DY):
        super().__init__(ENEMY_1_IMAGE, x, y, screen, dx, dy)

    def move(self):
        super().move()

    def update(self):
        super().update()


class EnemyType2(Enemy):
    def __init__(self, x, y, screen, dx=PLAYER_DX, dy=PLAYER_DY):
        super().__init__(ENEMY_2_IMAGE, x, y, screen, dx, dy)

    def move(self):
        super().move()

    def update(self):
        super().update()
