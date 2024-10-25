"""
    Defines the class that handles all of the user interface
"""

from presentation.interfaces import IMenu, IUserInterfaceHandler, IDisplay

class UserInterfaceHandler(IUserInterfaceHandler):
    """A generalized user interface handler for a display"""

    def __init__(self):
        self.__menus: list[IMenu] = {}

    def update(self, display: IDisplay):
        for menu in self.__menus.values():
            menu.update(display)

    def add_menu(self, menu: IMenu):
        self.__menus[menu.name] = menu

    def remove_menu(self, menu: IMenu):
        if self.__menus[menu.name]:
            self.__menus[menu.name] = None

    def get_menu(self, name: str):
        return self.__menus[name]
