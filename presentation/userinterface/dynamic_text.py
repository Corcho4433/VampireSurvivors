"""Defines a class used by dynamic texts"""

from pygame import Vector2
from presentation.userinterface.uicomponent import UIComponent
from presentation.userinterface.text import Text

class DynamicText(Text):
    """A text that can be placed on any place of the screen and not attached to a text"""

    def __init__(self, text: str, pos: Vector2, size: Vector2):
        self.__component = UIComponent(pos, size, (255, 255, 255), 0)

        super().__init__(text, self.__component)

    def update(self, display):
        super().update(display)
