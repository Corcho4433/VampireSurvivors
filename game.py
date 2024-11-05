"""This module defines the Game class."""

import logging

import pygame

import settings
from business.exceptions import DeadPlayerException
from business.handlers.collision_handler import CollisionHandler
from business.handlers.death_handler import DeathHandler
from business.world.interfaces import IGameWorld

from persistance.json_helpers import reset_file
from persistance.dao.json_player import JSONPlayerDAO
from persistance.dao.json_monster import JSONMonsterDAO
from persistance.dao.json_inventory import JSONInventoryDAO
from business.handlers.item_data_handler import ItemDataHandler
from persistance.dao.json_collectibles import JSONCollectibleDAO

from presentation.exceptions import SavedGameException
from presentation.interfaces import IDisplay, IInputHandler

ItemDataHandler.get_all_items()

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
        self.__collectibles_dao = JSONCollectibleDAO(settings.SAVE_FILE_PATH)

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

    def save(self):
        """Save the player's progress in game"""

        player = self.__world.player

        self.__inventory_dao.clear_inventory()
        for item in player.inventory.get_items():
            self.__inventory_dao.add_item(item)

        self.__monster_dao.clear_monsters()
        for monster in self.__world.monsters:
            self.__monster_dao.add_monster(monster)

        self.__collectibles_dao.clear_collectibles()
        for collectible in self.__world.collectibles:
            self.__collectibles_dao.add_collectible(collectible)

        self.__player_dao.add_player(player)

    def __load_data(self, player):
        self.__world.assign_player(player, self.__player_dao.get_time())

        for monster in self.__monster_dao.get_all_monsters():
            self.__world.add_monster(monster)

        for collectible in self.__collectibles_dao.get_all_collectibles():
            self.__world.add_collectible(collectible)

        player.assign_world(self.__world)
        player.take_damage(player.health-self.__player_dao.get_health())

    def run(self, player):
        """Starts the game loop."""
        self.__logger.debug("Starting the game loop.")
        self.__load_data(player)

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
                reset_file(settings.SAVE_FILE_PATH)
            except SavedGameException:
                self.__running = False
                self.save()
