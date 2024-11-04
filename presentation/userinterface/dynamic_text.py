"""
    Defines a class used by dynamic texts
"""

from pygame import Vector2
from presentation.userinterface.uicomponent import UIComponent
from presentation.userinterface.text import Text

class DynamicText(Text):
    """A text that can be placed on any place of the screen and not attached to a text"""

    def __init__(self, text: str, pos: Vector2, font_size: int=48, color: tuple[int, int, int]=(255, 255, 255), bold=Text.DEFAULT_BOLD, font=Text.DEFAULT_FONT):
        self.__component = UIComponent(pos, Vector2(), (255, 255, 255), 0)

        super().__init__(text, self.__component, font_size, color, font=font, bold=bold)

    def __str__(self):
        return f'DYNAMICTEXT::{self.text}'
