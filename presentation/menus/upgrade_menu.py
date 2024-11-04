"""Class that defines all of the buttons inside the """

from pygame import Vector2, time
import random
import settings

from presentation.menus.menu import Menu
from presentation.userinterface.uicomponent import UIComponent
from presentation.userinterface.button import Button
from presentation.userinterface.text import Text
from presentation.userinterface.dynamic_text import DynamicText
from business.world.interfaces import IGameWorld
from business.progression.interfaces import IUpgrade

class UpgradeMenu(Menu):
    """An upgrades menu"""

    def __init__(self, world: IGameWorld):
        super().__init__("Upgrade")

        self.__world: IGameWorld = world
        self.__upgrade_buttons = []

        self.set_active(False)

    def update(self, display):
        super().update(display)

        for object_upgrade in self.__upgrade_buttons:
            button = object_upgrade[0]
            upgrade_data = object_upgrade[1]

            factor = min((time.get_ticks() - button.hover_time)/100, 1)
            size = button.original_properties['size']
            pos = button.original_properties['pos']

            if button.is_hovering():
                origin = button.original_properties['color']
                pos = Vector2(button.pos.x + ((pos.x + size.x * .05) - button.pos.x) * factor, button.pos.y + ((pos.y - size.y*0.0125) - button.pos.y) * factor)
                size = Vector2(button.size.x + (size.x * 0.9 - button.size.x) * factor, button.size.y + (size.y * 1.025 - button.size.y) * factor)

                button.change_color((origin[0] + 25, origin[2] + 25, origin[2] + 25))
            else:
                pos = Vector2(button.pos.x + (pos.x - button.pos.x) * factor, button.pos.y + (pos.y - button.pos.y) * factor)
                size = Vector2(button.size.x + (size.x - button.size.x) * factor, button.size.y + (size.y - button.size.y) * factor)

                button.change_color(button.original_properties['color'])

            button.resize(size)
            button.move(pos)

            if button.is_clicked():
                self.__world.set_upgrade_menu_active(False)
                if upgrade_data == 'skip':
                    break

                self.__handle_button_presses(upgrade_data)

                break

    def __handle_button_presses(self, data: tuple[str]):
        item = self.__world.player.inventory.get_item(data[0])

        if item:
            item.upgrade()
        
        self.__world.player.apply_perks(heal=True)

    def draw(self):
        title = DynamicText("UPGRADE MENU", Vector2(settings.SCREEN_WIDTH // 2, 30), bold=True)
        background = UIComponent(Vector2(), Vector2(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), (0, 0, 0), 120)

        outline = UIComponent(Vector2(settings.SCREEN_WIDTH // 4 - 20, 0), Vector2(settings.SCREEN_WIDTH // 2 + 40, settings.SCREEN_HEIGHT), (10, 10, 35), 255)
        background_middle = UIComponent(Vector2(settings.SCREEN_WIDTH // 4, 0), Vector2(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT), (0, 0, 10), 255)

        self.add_component(outline)
        self.add_component(background_middle)
        self.add_component(background)
        self.add_component(title)

    def __clean_objects(self):
        self.__upgrade_buttons = []

        for object_component in self.components:
            self.remove_component(object_component)

    def __parse_items(self) -> list[tuple]:
        player = self.__world.player
        items = player.inventory.get_items()
        choices = []
        choosen = []

        for i in range(len(items)):
            item = items[i]
            choices.append((item.name, item.get_next_upgrade()))

        for i in range(min(3, len(items))):
            new_choice = random.choice(choices)

            choices.remove(new_choice)
            choosen.append(new_choice)

        return choosen

    
    def render_options(self):
        """Renders the options for the upgrade menu"""
        self.__clean_objects()
        self.draw()

        player = self.__world.player
        possible_upgrades = self.__parse_items() #[("default_gun", )] # ('weapon', next_upgrade)

        count = -1
        for upgrade_to_show in possible_upgrades:
            count += 1

            type_upgrade = upgrade_to_show[0]
            upgrade_object = upgrade_to_show[1]
            item = player.inventory.get_item(type_upgrade)

            y_pos = 100 + 270 * (count)/len(possible_upgrades)

            new_text = DynamicText(f"{type_upgrade.capitalize()}: Level {item.level} > Level {item.level + 1}", Vector2(settings.SCREEN_WIDTH // 2, y_pos - 10), 24)
            new_button = Button(Vector2(0, y_pos), Vector2(settings.SCREEN_WIDTH, 60), (0, 0, 20))
            description = upgrade_object.description if isinstance(upgrade_object, IUpgrade) else 'MAX UPGRADES'

            new_button.attach_text(Text(description, new_button))

            self.__upgrade_buttons.append((new_button, upgrade_to_show))
            self.add_component(new_text)
            self.add_component(new_button)

        skip_button = Button(Vector2(settings.SCREEN_WIDTH // 2 - 100, 400), Vector2(200, 35), (200, 30, 30))
        skip_button.attach_text(Text("Skip", skip_button, font_size=24, bold=True))

        self.__upgrade_buttons.append((skip_button, 'skip'))
        self.add_component(skip_button)

    def set_active(self, state):
        super().set_active(state)

        if state:
            self.render_options()
        else:
            self.__clean_objects()
