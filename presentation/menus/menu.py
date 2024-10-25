"""Defines the root class for all menu interfaces such as pause, hud, etc."""

from presentation.interfaces import IMenu, IUIComponent, IDisplay

class Menu(IMenu):
    """One of the user interface menus"""

    def __init__(self, name: str):
        self.__components: list[IUIComponent] = []
        self.__active = True
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def update(self, display: IDisplay):
        if not self.__active:
            return

        for component in self.__components:
            component.update(display)

    def set_active(self, state: bool):
        self.__active = state

    def add_component(self, component):
        self.__components.append(component)

    def remove_component(self, component):
        self.__components.remove(component)
