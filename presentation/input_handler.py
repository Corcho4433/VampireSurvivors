"""This module contains the InputHandler class, which handles user input for the game."""

import pygame
from pygame import Vector2

from business.handlers.position_handler import PositionHandler

from pygame import K_w as Key_w, K_d as Key_d, K_a as Key_a, K_s as Key_s, KEYDOWN,K_r as Key_r, K_ESCAPE #pylint: disable=E0611

from business.world.game_world import GameWorld
from presentation.interfaces import IInputHandler


class InputHandler(IInputHandler):
    """Handles user input for the game."""

    def __init__(self, world: GameWorld):
        self.__world = world
        self.__events = []

    def __get_player_direction_inputs(self, keys):
        dx, dy = 0, 0

        if keys[Key_w]:
            dy -= 1

        if keys[Key_s]:
            dy += 1

        if keys[Key_a]:
            dx -= 1

        if keys[Key_d]:
            dx += 1

        new_vector = Vector2(dx, dy)
        normalized = new_vector.normalize() if new_vector.magnitude() > 0 else Vector2(0, 0)

        dx = normalized.x * self.__world.simulation_speed
        dy = normalized.y * self.__world.simulation_speed

        new_direction_vector = Vector2(dx, dy)
        if not PositionHandler.is_position_within_boundaries(self.__world.player.pos + (new_direction_vector * 8)):
            return Vector2()

        return new_direction_vector

    def __check_pause(self):
        for event in self.__events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.__world.toggle_pause()
                self.__events.remove(event)

    def __check_slow_ability(self):
        for event in self.__events:
            if event.type == KEYDOWN and event.key == Key_r:
                self.__world.slow_down_enemies()
                self.__events.remove(event)

    def add_event(self, event):
        self.__events.append(event)

    def reset_events(self):
        self.__events = []

    def process_input(self):
        keys = pygame.key.get_pressed()
        direction = self.__get_player_direction_inputs(keys)

        self.__check_pause()
        self.__check_slow_ability()
        self.__world.player.move(direction)
