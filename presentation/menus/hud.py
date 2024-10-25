"""Defines the player Heads Up Display (HUD) for short"""

from pygame import Vector2

from presentation.menus.menu import Menu
#from presentation.userinterface.button import Button
from presentation.userinterface.dynamic_text import DynamicText

class HUD(Menu):
    """The heads up display that shows info such as exp bar etc"""

    def __init__(self, world):
        super().__init__("HUD")

        self.__world = world
        self.__exp_text: DynamicText = None

        self.draw()

    def update(self, display):
        super().update(display)

        player = self.__world.player
        self.__exp_text.change(f"XP: {player.experience}/{player.experience_to_next_level}")

    def draw(self):
        self.__exp_text = DynamicText("PAUSE MENU", Vector2(0, 0), Vector2(120, 50))

        self.add_component(self.__exp_text)
