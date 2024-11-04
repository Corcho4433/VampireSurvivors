"""
    Defines the root class used for any UI Component varying from a button to a background
"""

from pygame import Vector2, Rect, draw, Surface, SRCALPHA, error #pylint: disable=E0611
from presentation.interfaces import IDynamicUIComponent, IDisplay

class UIComponent(IDynamicUIComponent):
    """An ui component"""

    def __init__(self, pos: Vector2, size: Vector2, color: tuple[int, int, int], opacity: int):
        self.__pos = pos
        self.__size = size
        self.__color = color
        self.__active = True
        self.__opacity = opacity
        self.__original_properties = {'color': color, 'size': size, 'pos':pos}

        self.change_color(color)
        self.__make_rect()

    @property
    def original_properties(self):
        return self.__original_properties

    def set_active(self, state: bool):
        self.__active = state

    def draw(self) -> Surface:
        color = (self.__color[0], self.__color[1], self.__color[2], self.__opacity)
        shape_surf = Surface(self.__rect.size, SRCALPHA)
        draw.rect(shape_surf, color, shape_surf.get_rect())

        return shape_surf

    def update(self, display: IDisplay):
        try:
            shape_surf = self.draw()

            display.screen.blit(shape_surf, self.__rect)
        except error as err:
            print("Error on pygame:", err)

    def move(self, pos: Vector2):
        self.__pos = pos
        self.__make_rect()

    def resize(self, size: Vector2):
        self.__size = size
        self.__make_rect()

    def change_color(self, new_color):
        new_color = (min(255, new_color[0]), min(255, new_color[1]), min(255, new_color[2]))
        self.__color = new_color

    def change_opacity(self, opacity: int):
        if opacity > 255 or opacity < 0:
            return

        self.__opacity = opacity

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
    def opacity(self) -> int:
        return self.__opacity

    @property
    def rect(self) -> Rect:
        return self.__rect

    def __make_rect(self):
        self.__rect: Rect = Rect(self.__pos.x, self.__pos.y, self.__size.x, self.__size.y)

    def __str__(self):
        return f'COMPONENT::{self.__hash__()}'
