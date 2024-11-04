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

from business.progression.item_factory import ItemFactory
from business.handlers.item_data_handler import ItemDataHandler

class UpgradeMenu(Menu):
    """An upgrades menu"""

    ADD_ITEM_CASE = 1
    UPGRADE_ITEM_CASE = 2

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
                pos = Vector2(button.pos.x + ((pos.x - size.x * .05) - button.pos.x) * factor, button.pos.y + ((pos.y - size.y*0.0125) - button.pos.y) * factor)
                size = Vector2(button.size.x + (size.x * 1.1 - button.size.x) * factor, button.size.y + (size.y * 1.025 - button.size.y) * factor)

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
        match data[1]:
            case self.ADD_ITEM_CASE:
                new_item = ItemFactory.create_item(data[0])

                self.__world.player.inventory.add_item(new_item)
                self.__world.player.apply_perks(heal=True)
            case self.UPGRADE_ITEM_CASE:
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
        items = ItemDataHandler.get_all_items()
        choices = []
        choosen = []

        for item_index in enumerate(items):
            item = items[item_index[0]]
            obj_type = self.ADD_ITEM_CASE

            has_item = self.__world.player.inventory.get_item(item[0])
            if has_item is not None:
                obj_type = self.UPGRADE_ITEM_CASE

            choices.append((item[0], obj_type))

        for _ in range(min(3, len(items))):
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

            item_name = upgrade_to_show[0].replace("_", " ")
            action_type = upgrade_to_show[1]
            item = player.inventory.get_item(upgrade_to_show[0])

            y_pos = 100 + 300 * (count)/len(possible_upgrades)
            level_text = "Obtain Item"
            description = f"Unlock the item {item_name.capitalize()}"

            if item and action_type == self.UPGRADE_ITEM_CASE:
                level_text = f"{item_name.capitalize()}: Level {item.level} > Level {item.level + 1}"

                if item.get_next_upgrade():
                    description = item.get_next_upgrade().description
                else:
                    description = "MAX LEVEL"

            new_text = DynamicText(level_text, Vector2(settings.SCREEN_WIDTH // 2, y_pos - 10), 24)
            new_button = Button(Vector2(settings.SCREEN_WIDTH//4, y_pos), Vector2(settings.SCREEN_WIDTH // 2, 60), (0, 0, 20))

            new_button.attach_text(Text(description, new_button, 20))

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
