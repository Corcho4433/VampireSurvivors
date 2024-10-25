"""Defines the class text used by UI components"""

import pygame
from presentation.interfaces import IText, IUIComponent

class Text(IText):
    """Assignable text to a button or uicomponent"""

    def __init__(self, text: str, component: IUIComponent, font_size: int=48, color: tuple[int, int, int]=(255, 255, 255)):
        self.__text = text
        self.__color = color
        self.__component = component
        self.__font_size = font_size
        self.__active = True

    def update(self, display):
        font = pygame.font.SysFont(None, self.__font_size)
        text_object = font.render(self.__text, True, self.__color)
        pos = self.__component.pos
        size = self.__component.size
        rect = text_object.get_rect(center=(pos.x + size.x//2, pos.y + size.y//2))

        display.screen.blit(text_object, rect)

    @property
    def active(self):
        return self.__active

    def set_active(self, state):
        self.__active = state

    def change(self, text: str):
        self.__text = text
