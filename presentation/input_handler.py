"""This module contains the InputHandler class, which handles user input for the game."""

import pygame

from business.world.game_world import GameWorld
from presentation.interfaces import IInputHandler


class InputHandler(IInputHandler):
    """Handles user input for the game."""

    def __init__(self, world: GameWorld):
        self.__world = world

    def __get_player_direction_inputs(self, keys):
        dx, dy = 0, 0

        if keys[pygame.K_w]:
            dy -= 1

        if keys[pygame.K_s]:
            dy += 1

        if keys[pygame.K_a]:
            dx -= 1
            
        if keys[pygame.K_d]:
            dx += 1

        return pygame.Vector2(dx, dy)

    def process_input(self):
        keys = pygame.key.get_pressed()
        dir = self.__get_player_direction_inputs(keys)

        self.__world.player.move(dir)