"""Class that defines all of the buttons inside the """

from pygame import Vector2, time
import settings

from presentation.menus.menu import Menu
from presentation.userinterface.uicomponent import UIComponent
from presentation.userinterface.button import Button
from presentation.userinterface.text import Text
from presentation.userinterface.dynamic_text import DynamicText
from presentation.exceptions import SavedGameException

class PauseMenu(Menu):
    """A pause menu for the game"""

    def __init__(self, world):
        super().__init__("Pause")

        self.__quit_button: Button = None
        self.__resume_button: Button = None
        self.__world = world

        self.set_active(False)
        self.draw()

    def update(self, display):
        super().update(display)

        # Hovering
        quit_factor = min((time.get_ticks() - self.__quit_button.hover_time)/100, 1)
        resume_factor = min((time.get_ticks() - self.__resume_button.hover_time)/200, 1)

        if self.__quit_button.is_hovering():
            size = self.__quit_button.size

            self.__quit_button.resize(Vector2(size.x + (280 - size.x) * quit_factor, size.y + (67 - size.y) * quit_factor))
            self.__quit_button.move(Vector2(settings.SCREEN_WIDTH // 2 - self.__quit_button.size.x//2, 100 - (3.5 * quit_factor)))
            self.__quit_button.change_color((160, 120, 110))
        else:
            size = self.__quit_button.size

            self.__quit_button.resize(Vector2(size.x + (250 - size.x) * quit_factor, size.y + (60 - size.y) * quit_factor))
            self.__quit_button.move(Vector2(settings.SCREEN_WIDTH // 2 - self.__quit_button.size.x//2, 100 - (3.5 * (1 - quit_factor))))
            self.__quit_button.change_color((100, 100, 110))


        if self.__resume_button.is_hovering():
            size = self.__resume_button.size

            self.__resume_button.resize(Vector2(size.x + (280 - size.x) * resume_factor, size.y + (67 - size.y) * resume_factor))
            self.__resume_button.move(Vector2(settings.SCREEN_WIDTH // 2 - self.__resume_button.size.x//2, 200 - (3.5 * resume_factor)))
            self.__resume_button.change_color((130,130,160))
        else:
            size = self.__resume_button.size

            self.__resume_button.resize(Vector2(size.x + (250 - size.x) * resume_factor, size.y + (60 - size.y) * resume_factor))
            self.__resume_button.move(Vector2(settings.SCREEN_WIDTH // 2 - self.__resume_button.size.x//2, 200 - (3.5 * (1 - resume_factor))))
            self.__resume_button.change_color((100, 100, 110))

        # Clicking
        if self.__quit_button.is_clicked():
            raise SavedGameException

        if self.__resume_button.is_clicked():
            self.__world.toggle_pause()

    def draw(self):
        title = DynamicText("PAUSE MENU", Vector2(settings.SCREEN_WIDTH // 2, 25))
        background = UIComponent(Vector2(), Vector2(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), (0, 0, 10), 90)
        self.__quit_button = Button(Vector2(settings.SCREEN_WIDTH // 2 - 125, 100), Vector2(250, 60), (100, 100, 110))
        self.__resume_button = Button(Vector2(settings.SCREEN_WIDTH // 2 - 125, 200), Vector2(250, 60), (100, 100, 110))

        self.__quit_button.attach_text(Text("Save & Close", self.__quit_button))
        self.__resume_button.attach_text(Text("Continue", self.__resume_button))

        self.add_component(background)
        self.add_component(self.__quit_button)
        self.add_component(self.__resume_button)
        self.add_component(title)
