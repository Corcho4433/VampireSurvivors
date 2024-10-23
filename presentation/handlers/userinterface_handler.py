"""
    Defines the class that handles all of the user interface
"""

from presentation.interfaces import IUIComponent, IUserInterfaceHandler

class UserInterfaceHandler(IUserInterfaceHandler):
    def __init__(self):
        self.__components: list[IUIComponent] = []

    def update(self):
        for component in self.__components:
            component.update()

    def add_component(self, component: IUIComponent):
        self.__components.append(component)

    def remove_component(self, component: IUIComponent):
        self.__components.remove(component)
    
