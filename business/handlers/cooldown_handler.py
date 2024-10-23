"""This module contains the CooldownHandler class."""

import pygame


class CooldownHandler:
    """A handler for cooldowns."""

    def __init__(self, cooldown_time: float):
        """Starts up a new cooldown handler for any task
        
            Args:
                cooldown_time (float): The time in seconds
        """
        self.__last_action_time = pygame.time.get_ticks()
        self.__cooldown_time = cooldown_time

    def is_action_ready(self):
        """Check if the action is ready to be performed."""
        current_time = pygame.time.get_ticks()
        return current_time - self.__last_action_time >= (self.__cooldown_time * 1000)

    def put_on_cooldown(self):
        """Put the action on cooldown."""
        self.__last_action_time = pygame.time.get_ticks()

    def change_time(self, new: int):
        """
            Changes the time of the cooldown
            Args:
                cooldown_time (float): The time in seconds
        """
        self.__cooldown_time = new
