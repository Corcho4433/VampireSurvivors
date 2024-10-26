"""Class that defines all of the buttons inside the """

from pygame import Vector2
import settings

from presentation.menus.menu import Menu
from presentation.userinterface.uicomponent import UIComponent
from presentation.userinterface.button import Button
from presentation.userinterface.text import Text
from presentation.userinterface.dynamic_text import DynamicText
from business.world.interfaces import IGameWorld

class UpgradeMenu(Menu):
    """An upgrades menu"""

    def __init__(self, world: IGameWorld):
        super().__init__("Upgrade")

        self.__world: IGameWorld = world
        self.__upgrade_buttons = []

        self.set_active(False)
        self.draw()

    def update(self, display):
        super().update(display)

        for object_button in self.__upgrade_buttons:
            if object_button.is_clicked():
                self.__world.set_upgrade_menu_active(False)

                break

    def draw(self):
        title = DynamicText("UPGRADE MENU", Vector2(0, 0), Vector2(settings.SCREEN_WIDTH, 50))
        background = UIComponent(Vector2(), Vector2(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), (0, 0, 0), 125)

        self.add_component(background)
        self.add_component(title)

    def render_options(self):
        """Renders the options for the upgrade menu"""

        for object_component in self.__upgrade_buttons:
            self.remove_component(object_component)

        # player = self.__world.player
        # upgrades = player.weapon_upgrades

        new_button = Button(Vector2(settings.SCREEN_WIDTH//2 - 125, 200), Vector2(250, 60), (255, 255, 255))
        new_button.attach_text(Text("Upgrade 1 Test", new_button, color=(0, 0, 0)))

        self.__upgrade_buttons.append(new_button)
        self.add_component(new_button)

    def set_active(self, state):
        super().set_active(state)

        if state:
            self.render_options()
