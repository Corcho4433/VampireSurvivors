"""Class that defines all of the buttons inside the """

from pygame import Vector2, time
import settings

from presentation.menus.menu import Menu
from presentation.userinterface.uicomponent import UIComponent
from presentation.userinterface.button import Button
from presentation.userinterface.text import Text
from presentation.userinterface.dynamic_text import DynamicText

class PauseMenu(Menu):
    """A pause menu for the game"""

    def __init__(self, world):
        super().__init__("Pause")

        self.__quit_button: Button = None
        self.__resume_button: Button = None
        self.__world = world
        self.__last_hover = time.get_ticks()
        self.__last_hover_2 = time.get_ticks()

        self.set_active(False)
        self.draw()

    def update(self, display):
        super().update(display)

        # Hovering
        if self.__quit_button.is_hovering():
            factor = min((time.get_ticks() - self.__last_hover)/100, 1)

            self.__quit_button.resize(Vector2(250 + 30 * factor, 60 + 7 * factor))
            self.__quit_button.move(Vector2(settings.SCREEN_WIDTH // 2 - self.__quit_button.size.x//2, 100 - (3.5 * factor)))
            self.__quit_button.change_color((160, 120, 110))
        else:
            self.__last_hover = time.get_ticks()

            self.__quit_button.resize(Vector2(250, 60))
            self.__quit_button.move(Vector2(settings.SCREEN_WIDTH // 2 - self.__quit_button.size.x//2, 100))
            self.__quit_button.change_color((100, 100, 110))

        if self.__resume_button.is_hovering():
            factor = min((time.get_ticks() - self.__last_hover_2)/200, 1)

            self.__resume_button.change_color((130,130,160))
        else:
            self.__last_hover_2 = time.get_ticks()
            self.__resume_button.change_color((100, 100, 110))

        # Clicking
        if self.__quit_button.is_clicked():
            quit()

        if self.__resume_button.is_clicked():
            self.__world.toggle_pause()

    def draw(self):
        title = DynamicText("PAUSE MENU", Vector2(0, 0), Vector2(settings.SCREEN_WIDTH, 50))
        background = UIComponent(Vector2(), Vector2(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), (0, 0, 10), 90)
        self.__quit_button = Button(Vector2(settings.SCREEN_WIDTH // 2 - 125, 100), Vector2(250, 60), (100, 100, 110))
        self.__resume_button = Button(Vector2(settings.SCREEN_WIDTH // 2 - 125, 200), Vector2(250, 60), (100, 100, 110))

        self.__quit_button.attach_text(Text("Close", self.__quit_button))
        self.__resume_button.attach_text(Text("Continue", self.__resume_button))
        
        self.add_component(background)
        self.add_component(self.__quit_button)
        self.add_component(self.__resume_button)
        self.add_component(title)
