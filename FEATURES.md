# Planned Features

This document outlines the features planned for the game. Each feature will be implemented in stages, with testing conducted at each stage to ensure the functionality works as expected.

## 1. Implement Basic Enemy Class and Variations

- [x] Create a base `Enemy` class in a separate file (e.g., `enemy.py`).
- [x] Implement at least two different enemy types by subclassing the `Enemy` class (e.g., `EnemyType1`, `EnemyType2`).
- Add movement and behavior logic for each enemy type.

## 2. Implement Shooting Functionality for the Player

- Create a `Projectile` class in a separate file (e.g., `projectile.py`).
- Add a method to the `Player` class for firing projectiles (e.g., `fire_projectile`).
- Handle projectile movement and collision detection with enemies.
- Display a score on the screen.

## 3. Implement Weapon Upgrades

- Modify the `Player` class to store information about the current weapon.
- Implement different weapon types with varying projectile properties (e.g., speed, damage).
- Add logic to change the player's weapon when they hit certain types of enemies or collect power-ups.

## 4. Implement Start/Pause Screen

- Create a new function or class to handle the start/pause screen (e.g., `start_pause_screen`).
- Add buttons or menu options to start the game, change game settings, or exit.
- Pause the game by stopping the main game loop and displaying the start/pause screen.

## 5. Add Game Preferences

- Create a separate file or class to store game settings (e.g., `game_settings.py` or `GameSettings` class).
- Add functionality to the start/pause screen to modify these settings (e.g., game speed, graphics, and colors).
- Apply the modified settings to the main game loop and other relevant parts of the code.
\