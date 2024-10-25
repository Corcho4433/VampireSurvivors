"""
    This module defines the root classes used for User Interface
"""

import pygame

from presentation.userinterface.uicomponent import UIComponent
from presentation.interfaces import IButton, IText

class Button(UIComponent, IButton):
    """A clickable button in a user interface"""

    def __init__(self, pos: pygame.Vector2, size: pygame.Vector2, color: tuple[int, int, int]):
        super().__init__(pos, size, color, 255)

        self.__text: IText = None
        self.__clicked = False
        self.__released = True

    def update(self, display):
        super().update(display)

        if self.__text:
            self.__text.update(display)

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and self.__released:
                self.__clicked = True
                self.__released = False
            elif not pygame.mouse.get_pressed()[0]:
                self.__released = True

    def is_clicked(self):
        state = self.__clicked
        if state:
            self.__clicked = False

        return state

    def attach_text(self, text: IText) -> None:
        self.__text = text
