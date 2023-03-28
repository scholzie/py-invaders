# game.py
import random
from enemy import EnemyType1, EnemyType2
from player import Player
from constants import *


class Game:

    def __init__(self):
        self.screen = None
        self.lasers = None
        self.enemies = None
        self.player = None
        self.running = False

        self.init_pygame()
        self.DEFAULT_FONT = pygame.font.SysFont(None, 32)
        self.directions_text = self.DEFAULT_FONT.render("Use arrow keys to move. Press ESC to quit.", True,
                                                        (255, 255, 255))
        self.init_entities()

    def init_pygame(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(GAME_TITLE)
        pygame.display.set_icon(pygame.image.load(GAME_ICON))

    def init_entities(self):
        self.player = Player(PLAYER_IMAGE, self.screen.get_width() // 2,
                             self.screen.get_height() - self.screen.get_height() // 3, self.screen)
        self.enemies = self.create_enemies()
        self.lasers = []

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

    @staticmethod
    def check_collision(obj1, obj2):
        obj1_rect = obj1.image.get_rect(topleft=(obj1.x, obj1.y))
        obj2_rect = obj2.image.get_rect(topleft=(obj2.x, obj2.y))
        return obj1_rect.colliderect(obj2_rect)

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.process_event(event)

            self.handle_key_events()

            self.screen.fill((200, 200, 200))
            # screen.fill((0, 0, 0))
            # screen.blit(DEFAULT_BACKGROUND, (0, 0))

            directions_text_rect = self.directions_text.get_rect(center=(self.screen.get_width() / 2, 50))
            self.screen.blit(self.directions_text, directions_text_rect)

            for laser in self.lasers:
                laser.move_y(-1)
                laser.draw()
                for enemy in self.enemies:
                    if self.check_collision(laser, enemy):
                        self.enemies.remove(enemy)
                        self.lasers.remove(laser)
                        break

            for enemy in self.enemies:
                enemy.update()
                enemy.draw()

            self.player.draw()
            pygame.display.update()
