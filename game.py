# game.py
import random

import pygame

from enemy import EnemyType1, EnemyType2
from player import Player
from constants import ENEMY_COLS, ENEMY_ROWS, PLAYER_IMAGE


class Game:

    def __init__(self, screen, player_image=PLAYER_IMAGE):
        self.screen = screen
        self.player = Player(PLAYER_IMAGE, self.screen.get_width() // 2,
                             self.screen.get_height() - self.screen.get_height() // 3, self.screen)
        self.enemies = self.create_enemies()
        self.lasers = []
        self.running = True

    def init_pygame(self):
        pass

    def init_entities(self):
        pass

    def create_enemies(self):
        enemies = []
        for row in range(ENEMY_ROWS):
            enemy_type = random.choice([EnemyType1, EnemyType2])
            for col in range(ENEMY_COLS):
                enemy = enemy_type(col * 60 + 100, row * 50 + 50, self.screen)
                enemies.append(enemy)
        return enemies

    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False

    def handle_key_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_x(-1)
        if keys[pygame.K_RIGHT]:
            self.player.move_x(1)
        if keys[pygame.K_UP]:
            self.player.move_y(-1)
        if keys[pygame.K_DOWN]:
            self.player.move_y(1)
        if keys[pygame.K_SPACE]:
            self.lasers.append(self.player.fire_laser())

    def check_collision(self, obj1, obj2):
        obj1_rect = obj1.image.get_rect(topleft=(obj1.x, obj1.y))
        obj2_rect = obj2.image.get_rect(topleft=(obj2.x, obj2.y))
        return obj1_rect.colliderect(obj2_rect)

    def run(self):
        running = True
        while running:
            screen.fill((200, 200, 200))
            # screen.fill((0, 0, 0))
            # screen.blit(DEFAULT_BACKGROUND, (0, 0))
            for event in pygame.event.get():
                self.process_event(event)

            directions_text = DEFAULT_FONT.render("Use arrow keys to move. Press ESC to quit.", True, (255, 255, 255))
            directions_text_rect = directions_text.get_rect(center=(screen.get_width() / 2, 50))
            screen.blit(directions_text, directions_text_rect)

            for laser in lasers:
                laser.move_y(-1)
                laser.draw()
                for enemy in enemies:
                    if check_collision(laser, enemy):
                        enemies.remove(enemy)
                        lasers.remove(laser)
                        break

            for enemy in enemies:
                enemy.update()
                enemy.draw()

            player.check_boundary()
            player.draw()
            pygame.display.update()