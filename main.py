# main.py
import sys
from constants import *
from player import Player

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

    # Game Loop
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(DEFAULT_BACKGROUND, (0, 0))
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

        player.check_boundary()
        player.draw()
        pygame.display.update()

    terminate()


if __name__ == '__main__':
    main()
