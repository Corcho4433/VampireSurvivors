"""
    Defines the class text used by UI components
    """

import pygame
from presentation.interfaces import IText, IUIComponent

class Text(IText):
    """Assignable text to a button or uicomponent"""

    DEFAULT_FONT = 'bahnschrift'
    DEFAULT_BOLD = False

    def __init__(self, text: str, component: IUIComponent,
                 font_size: int=48,
                 color: tuple[int, int, int]=(255, 255, 255),
                 font: str=DEFAULT_FONT,
                 bold=DEFAULT_BOLD,
                 align: tuple[float, float]=(0.5, 0.5)):
        self.__text = text
        self.__color = color
        self.__component = component
        self.__font_size = font_size
        self.__active = True
        self.__font = font
        self.__bold = bold
        self.__align = align

    def update(self, display):
        x_div, y_div = 1 / self.__align[0], 1 / self.__align[1]

        font = pygame.font.SysFont(self.__font, int(self.__font_size * 0.75), self.__bold)
        text_object = font.render(self.__text, True, self.__color)
        pos = self.__component.pos
        size = self.__component.size
        rect = text_object.get_rect(center=(pos.x + size.x//x_div, pos.y + size.y//y_div))

        display.screen.blit(text_object, rect)

    @property
    def active(self):
        return self.__active

    @property
    def text(self):
        return self.__text

    def set_active(self, state):
        self.__active = state

    def change(self, text: str):
        self.__text = text

    def __str__(self):
        return f'TEXT::{self.__hash__()}'
