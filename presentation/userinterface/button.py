"""
    This module defines the root classes used for User Interface
"""


from presentation.userinterface.uicomponent import UIComponent
from presentation.interfaces import IButton
from pygame import Vector2

class Button(UIComponent, IButton):
    """A clickable button in a user interface"""

    def __init__(self, pos: Vector2, size: Vector2):
        super().__init__(pos, size)