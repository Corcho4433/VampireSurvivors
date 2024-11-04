"""Defines the class "ImageComponent", which is a component that also
    allows for images to be shown in it
"""

import pygame
from pygame import Vector2, Surface, SRCALPHA #pylint: disable=E0611

from presentation.userinterface.uicomponent import UIComponent
from presentation.interfaces import IImageComponent

class ImageComponent(UIComponent, IImageComponent):
    """A component that also holds an image"""

    def __init__(self, image_path: str,
                 pos: Vector2,
                 size: Vector2,
                 color: tuple[int, int, int]=(255, 255, 255),
                 opacity: int=0):
        super().__init__(pos, size, color, opacity)

        self.__image_size = (size.x * 0.9,size.y * 0.9)
        self.__raw_image = pygame.image.load(image_path)
        self.__image = pygame.transform.scale(self.__raw_image, self.__image_size)

    def resize_image(self, new_size: Vector2):
        self.__image_size = (new_size.x, new_size.y)
        self.__image = pygame.transform.scale(self.__raw_image, self.__image_size)

    def draw(self) -> Surface:
        #color = (self.color[0], self.color[1], self.color[2], self.opacity)
        shape_surf = Surface(self.rect.size, SRCALPHA)

        shape_surf.blit(self.__image, self.image.get_rect())

        return shape_surf

    @property
    def image(self):
        return self.__image

    def __str__(self):
        return f'IMAGEUICOMPONENT::{self.__hash__()}'
