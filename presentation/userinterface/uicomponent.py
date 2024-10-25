"""
    Defines the root class used for any UI Component varying from a button to a background
"""

from pygame import Vector2, Rect, draw, Surface, SRCALPHA #pylint: disable=E0611
from presentation.interfaces import IDynamicUIComponent, IDisplay

class UIComponent(IDynamicUIComponent):
    """An ui component"""

    def __init__(self, pos: Vector2, size: Vector2, color: tuple[int, int, int], opacity: int):
        self.__pos = pos
        self.__size = size
        self.__color = color
        self.__active = True
        self.__opacity = opacity

        self.__make_rect()

    def set_active(self, state: bool):
        self.__active = state

    def update(self, display: IDisplay):
        color = (self.__color[0], self.__color[1], self.__color[2], self.__opacity)
        shape_surf = Surface(self.__rect.size, SRCALPHA)
        draw.rect(shape_surf, color, shape_surf.get_rect())

        display.screen.blit(shape_surf, self.__rect)

    def move(self, pos: Vector2):
        self.__pos = pos
        self.__make_rect()

    def resize(self, size: Vector2):
        self.__size = size
        self.__make_rect()

    def change_color(self, new_color):
        self.__color = new_color

    @property
    def active(self) -> bool:
        return self.__active

    @property
    def pos(self) -> Vector2:
        return Vector2(self.__pos.x, self.__pos.y)

    @property
    def size(self) -> Vector2:
        return Vector2(self.__size.x, self.__size.y)

    @property
    def color(self) -> tuple[int, int, int]:
        return self.__color

    @property
    def rect(self) -> Rect:
        return self.__rect

    def __make_rect(self):
        self.__rect: Rect = Rect(self.__pos.x, self.__pos.y, self.__size.x, self.__size.y)
