"""
    Defines the root class used for any UI Component varying from a button to a background
"""

from pygame import Vector2
from presentation.interfaces import IUIComponent

class UIComponent(IUIComponent):
    def __init__(self, pos: Vector2, size: Vector2):
        self.__pos = pos
        self.__size = size
        self.__active = True

    def set_visible(self, state: bool):
        self.__active = state

    def update():
        pass

    @property
    def active(self) -> bool:
        return self.__active

    @property
    def pos(self) -> Vector2:
        return Vector2(self.__pos.x, self.__pos.y)
    
    @property
    def size(self) -> Vector2:
        return Vector2(self.__size.x, self.__size.y)