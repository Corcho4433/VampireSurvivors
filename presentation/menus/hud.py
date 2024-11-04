"""Defines the player Heads Up Display (HUD) for short"""

from datetime import timedelta
from pygame import Vector2, time
from settings import SCREEN_WIDTH

from presentation.menus.menu import Menu
from presentation.userinterface.uicomponent import UIComponent
from presentation.userinterface.dynamic_text import DynamicText
from presentation.userinterface.image_component import ImageComponent

class HUD(Menu):
    """The heads up display that shows info such as exp bar etc"""

    def __init__(self, world):
        super().__init__("HUD")

        self.__world = world
        self.__exp_text: DynamicText = None
        self.__last_experience = 1
        self.__was_upgrading = False
        self.__last_change = time.get_ticks()
        self.__clock: DynamicText = None
        self.__items = []
        self.__last_inventory = []

        self.draw()

    def update(self, display):
        super().update(display)

        player = self.__world.player
        if player.experience != self.__last_experience:
            self.__last_experience = player.experience
            self.__last_change = time.get_ticks()

        factor = min((time.get_ticks() - self.__last_change)/500, 1)
        exp = player.experience

        if self.__world.upgrading:
            self.__was_upgrading = True
            exp = player.experience_to_next_level
        elif not self.__world.upgrading and self.__was_upgrading:
            self.__last_change = time.get_ticks()
            self.__was_upgrading = False

        self.__exp_text.change(f"XP: {player.experience}/{player.experience_to_next_level} | Level: {player.level}")
        goal_x_size = (exp/player.experience_to_next_level) * SCREEN_WIDTH
        size_x = self.__bar_fill.size.x

        self.__bar_fill.resize(Vector2(size_x + (goal_x_size - size_x) * factor, 20))
        self.__clock.change(str(timedelta(seconds=round(self.__world.clock_seconds))))

        self.__update_inventory()

    def draw(self):
        self.__exp_text = DynamicText("XP: 0/1 | Level: 1", Vector2(90, 11), 30)
        self.__clock = DynamicText("00:00", Vector2(SCREEN_WIDTH//2, 40), 40)
        self.__bar_fill = UIComponent(Vector2(), Vector2(0, 20), (20, 20, 140), 255)


        self.add_component(UIComponent(Vector2(), Vector2(SCREEN_WIDTH, 20), (0, 0, 10), 255))
        self.add_component(self.__bar_fill)
        self.add_component(self.__exp_text)
        self.add_component(self.__clock)

    def __update_inventory(self):
        full_inventory = self.__world.player.inventory.get_items()

        for item_component in self.__items:
            self.remove_component(item_component)

            del item_component

        self.__items = []

        amount = len(full_inventory)

        text_component = DynamicText("Inventory:",Vector2(41, 35), font_size=24)
        component_bg = UIComponent(Vector2(0, 46), Vector2(amount * 58 + 10, 62), (0, 0, 0), (100))

        self.__items.append(component_bg)
        self.add_component(component_bg)

        self.__items.append(text_component)
        self.add_component(text_component)

        count = 0
        for item in full_inventory:
            shown_level = f"Lv. {item.level}"
            if not item.get_next_upgrade():
                shown_level = "MAX"

            new_bg = UIComponent(Vector2(count * 57 + 10, 50), Vector2(54, 54), (0,0,0), 45)
            new_component = ImageComponent(f"./assets/{item.name}.png", Vector2(count * 59 + 10, 50), Vector2(50, 50))
            new_text = DynamicText(shown_level, Vector2(count * 59 + 45, 95), 18)

            #new_component.change_color((0,0,0))
            #new_component.change_opacity(100)

            self.__items.append(new_bg)
            self.__items.append(new_text)
            self.__items.append(new_component)

            self.add_component(new_bg)
            self.add_component(new_component)
            self.add_component(new_text)

            count += 1
