"""
    This module defines the GUI for the inventory
"""

import pygame

from presentation.menus.menu import Menu

class InventoryGui(Menu):
    """The inventory in a user interface"""

    def __init__(self):
        super().__init__("Inventory")
        self.draw()

    def update(self, display):
        super().update(display)

    def draw(self):
        pass