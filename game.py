"""This module defines the Game class."""

import logging

import pygame

import settings
from business.exceptions import DeadPlayerException
from business.handlers.collision_handler import CollisionHandler
from business.handlers.death_handler import DeathHandler
from business.world.interfaces import IGameWorld
from presentation.interfaces import IDisplay, IInputHandler
from persistance.dao.json_player import JSONPlayerDAO
from persistance.dao.json_monster import JSONMonsterDAO
from persistance.dao.json_inventory import JSONInventoryDAO

class Game:
    """
    Main game class.

    This is the game entrypoint.
    """

    def __init__(self, display: IDisplay, game_world: IGameWorld, input_handler: IInputHandler):
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__clock = pygame.time.Clock()
        self.__display = display
        self.__world = game_world
        self.__input_handler = input_handler
        self.__running = True
        self.__player_dao = JSONPlayerDAO(settings.SAVE_FILE_PATH)
        self.__monster_dao = JSONMonsterDAO(settings.SAVE_FILE_PATH)
        self.__inventory_dao = JSONInventoryDAO(settings.SAVE_FILE_PATH)

    def __process_game_events(self):
        self.__input_handler.reset_events()

        for event in pygame.event.get():
            # pygame.QUIT event means the user clicked X to close your window
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                self.__logger.debug("QUIT event detected")
                self.__running = False

            self.__input_handler.add_event(event)

    def create_player(self):
        """Creates the player instance from a DAO object"""

        return self.__player_dao.get_player()

    def create_monsters(self):
        """Creates all the in game monsters from a DAO object"""

        return self.__monster_dao.get_all_monsters()

    def create_inventory(self):
        """Creates the player inventory instance from a DAO object"""

        return self.__inventory_dao.get_inventory()

    def run(self, player):
        """Starts the game loop."""
        self.__logger.debug("Starting the game loop.")
        
        self.__world.assign_player(player)
        player.assign_world(self.__world)

        while self.__running:
            try:
                self.__process_game_events()
                self.__input_handler.process_input()
                self.__world.update()
                CollisionHandler.handle_collisions(self.__world)
                DeathHandler.check_deaths(self.__world)
                self.__display.render_frame()
                self.__clock.tick(settings.FPS)
            except DeadPlayerException:
                self.__running = False
