# main.py
import random
import sys
from constants import *
from player import Player
from enemy import EnemyType1, EnemyType2

pygame.init()
pygame.font.init()
DEFAULT_FONT = pygame.font.SysFont(None, 32)


def terminate():
    pygame.quit()
    sys.exit()


def process_event(e, player):
    if e.type == pygame.QUIT:
        terminate()
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_ESCAPE:
            terminate()


def main():
    # Screen Setup
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(GAME_TITLE)
    pygame.display.set_icon(pygame.image.load(GAME_ICON))

    # Player Setup
    player_image = os.path.join(SPRITE_DIR, 'player-ship.png')
    player = Player(player_image, 370, 480, screen)

    # enemy setup
    # Initially, we will have 11 enemies in a row, and 5 rows.
    # Each row will randomly choose either Enemy 1 or Enemy 2.
    # Both Enemy types will have the same stats for now.
    enemies = []
    for row in range(ENEMY_ROWS):
        enemy_type = random.choice([EnemyType1, EnemyType2])
        for col in range(ENEMY_COLS):
            enemy = enemy_type(col * 60 + 100, row * 50 + 50, screen)
            enemies.append(enemy)

    # Game Loop
    running = True
    while running:
        screen.fill((200, 200, 200))
        # screen.fill((0, 0, 0))
        # screen.blit(DEFAULT_BACKGROUND, (0, 0))
        for event in pygame.event.get():
            process_event(event, player)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_x(-1)
        if keys[pygame.K_RIGHT]:
            player.move_x(1)
        if keys[pygame.K_UP]:
            player.move_y(-1)
        if keys[pygame.K_DOWN]:
            player.move_y(1)

        directions_text = DEFAULT_FONT.render("Use arrow keys to move. Press ESC to quit.", True, (255, 255, 255))
        directions_text_rect = directions_text.get_rect(center=(screen.get_width() / 2, 50))
        screen.blit(directions_text, directions_text_rect)

        for enemy in enemies:
            enemy.update()
            enemy.draw()

        player.check_boundary()
        player.draw()
        pygame.display.update()

    terminate()


if __name__ == '__main__':
    main()
