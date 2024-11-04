#!/usr/bin/env python3
"""Runs the game"""
import logging
import pygame
import settings

from business.world.game_world import GameWorld
from business.world.monster_spawner import MonsterSpawner
from business.world.chest_spawner import ChestSpawner
from business.world.tile_map import TileMap
from game import Game
from presentation.display import Display
from presentation.input_handler import InputHandler
from presentation.exceptions import RetryGameException
from persistance.json_helpers import reset_file


def initialize_game_world(display):
    """Initializes the game world"""
    monster_spawner = MonsterSpawner()
    chest_spawner = ChestSpawner()
    tile_map = TileMap()
    return GameWorld(monster_spawner, chest_spawner, tile_map, display)


def main():
    """Main function to run the game"""
    # Initialize pygame
    pygame.init() #pylint: disable=E1101

    # Logging configuration
    logging.basicConfig(
        level=logging.INFO,  # Change between INFO, WARNING or DEBUG as needed
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Initialize the game objects
    display = Display()
    world = initialize_game_world(display)
    display.load_world(world)
    input_handler = InputHandler(world)

    # Create a game instance and start it
    game = Game(display, world, input_handler)

    player = game.create_player()
    player.assign_inventory(game.create_inventory())

    try:
        game.run(player)
    except RetryGameException:
        reset_file(settings.SAVE_FILE_PATH)
        main()

    # Properly quit Pygame
    pygame.quit() #pylint: disable=E1101


if __name__ == "__main__":
    main()
