"""
    The end screen of the game, shows a retry or close button
"""

from datetime import timedelta
from pygame import Vector2
import settings

from presentation.exceptions import RetryGameException
from presentation.menus.menu import Menu
from presentation.userinterface.text import Text
from presentation.userinterface.button import Button
from presentation.userinterface.uicomponent import UIComponent
from presentation.userinterface.dynamic_text import DynamicText

class GameOver(Menu):
    """The game over menu"""

    def __init__(self, world):
        super().__init__("GameOver")

        self.__world = world
        self.__retry_button = None
        self.__quit_button = None
        self.__background = UIComponent(Vector2(), Vector2(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), (0, 0, 10), 0) #pylint: disable=C0301

        self.add_component(self.__background)
        self.set_active(False)

    def set_bg_visibility(self, factor: int):
        """Change the visibility of the death screen background"""
        self.__background.change_opacity(170 * factor)

    def update(self, display):
        self.__background.update(display)
        super().update(display)

        if not self.active:
            return

        if self.__retry_button.is_clicked():
            raise RetryGameException

        if self.__quit_button.is_clicked():
            quit()

    def set_active(self, state):
        super().set_active(state)

        if state:
            self.draw()
        else:
            for component in self.components:
                self.components.remove(component)

            self.add_component(self.__background)

    def draw(self):
        time_text = f"Lasted: {str(timedelta(seconds=round(self.__world.clock_seconds)))}"
        damage_dealt_text = f"Total Damage: {self.__world.total_damage}" #pylint: disable=C0301

        title = DynamicText("GAME OVER", Vector2(settings.SCREEN_WIDTH // 2, 70), 60, color=(255, 100, 100), bold=True) #pylint: disable=C0301
        clock_text = DynamicText(time_text, Vector2(settings.SCREEN_WIDTH//2, 130), 45)
        damage_text = DynamicText(damage_dealt_text, Vector2(settings.SCREEN_WIDTH//2, 170), 45)
        middle = UIComponent(Vector2(settings.SCREEN_WIDTH // 4, 0), Vector2(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT), (0, 0, 10), 140)  #pylint: disable=C0301
        self.__quit_button = Button(Vector2(settings.SCREEN_WIDTH // 2 - 125, 240), Vector2(250, 60), (100, 100, 110)) #pylint: disable=C0301
        self.__retry_button = Button(Vector2(settings.SCREEN_WIDTH // 2 - 125, 340), Vector2(250, 60), (100, 100, 110)) #pylint: disable=C0301

        self.__quit_button.attach_text(Text("Quit", self.__quit_button))
        self.__retry_button.attach_text(Text("Retry", self.__retry_button))

        self.add_component(middle)
        self.add_component(self.__quit_button)
        self.add_component(self.__retry_button)
        self.add_component(clock_text)
        self.add_component(damage_text)
        self.add_component(title) #pylint: disable=C0301
