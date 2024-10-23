"""This module contains the InputHandler class, which handles user input for the game."""

import settings
import pygame

from business.world.game_world import GameWorld
from presentation.interfaces import IInputHandler


class InputHandler(IInputHandler):
    """Handles user input for the game."""

    def __init__(self, world: GameWorld):
        self.__world = world
        self.__events = []

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

        dx *= self.__world.simulation_speed
        dy *= self.__world.simulation_speed

        return pygame.Vector2(dx, dy)
    
    def __check_pause(self):
        for event in self.__events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.__world.toggle_pause()

            self.__events.remove(event)

    def add_event(self, event):
        self.__events.append(event)

    def reset_events(self):
        self.__events = []

    def process_input(self):
        keys = pygame.key.get_pressed()
        dir = self.__get_player_direction_inputs(keys)

        self.__check_pause()
        self.__world.player.move(dir)