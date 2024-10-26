"""Defines the player Heads Up Display (HUD) for short"""

from pygame import Vector2, time
from settings import SCREEN_WIDTH
from datetime import timedelta

from presentation.menus.menu import Menu
from presentation.userinterface.uicomponent import UIComponent
from presentation.userinterface.dynamic_text import DynamicText

class HUD(Menu):
    """The heads up display that shows info such as exp bar etc"""

    def __init__(self, world):
        super().__init__("HUD")

        self.__world = world
        self.__exp_text: DynamicText = None
        self.__last_experience = 1
        self.__was_upgrading = False
        self.__last_change = time.get_ticks()
        self.__clock: DynamicText = None

        self.draw()

    def update(self, display):
        super().update(display)

        player = self.__world.player
        if player.experience != self.__last_experience:
            self.__last_experience = player.experience
            self.__last_change = time.get_ticks()

        factor = min((time.get_ticks() - self.__last_change)/500, 1)
        exp = player.experience

        if self.__world.upgrading:
            self.__was_upgrading = True
            exp = player.experience_to_next_level
        elif not self.__world.upgrading and self.__was_upgrading:
            self.__last_change = time.get_ticks()
            self.__was_upgrading = False

        self.__exp_text.change(f"XP: {player.experience}/{player.experience_to_next_level} | Level: {player.level}")
        goal_x_size = (exp/player.experience_to_next_level) * SCREEN_WIDTH
        size_x = self.__bar_fill.size.x

        self.__bar_fill.resize(Vector2(size_x + (goal_x_size - size_x) * factor, 20))
        self.__clock.change(str(timedelta(seconds=round(self.__world.clock_seconds))))

    def draw(self):
        self.__exp_text = DynamicText("XP: 0/1 | Level: 1", Vector2(90, 11), 30)
        self.__clock = DynamicText("00:00", Vector2(SCREEN_WIDTH//2, 40), 40)
        self.__bar_fill = UIComponent(Vector2(), Vector2(0, 20), (20, 20, 140), 255)


        self.add_component(UIComponent(Vector2(), Vector2(SCREEN_WIDTH, 20), (0, 0, 10), 255))
        self.add_component(self.__bar_fill)
        self.add_component(self.__exp_text)
        self.add_component(self.__clock)
