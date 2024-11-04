"""Module for displaying the game world."""

import pygame

import settings
from business.world.interfaces import IGameWorld
from presentation.camera import Camera
from presentation.interfaces import IDisplay
from presentation.tileset import Tileset
from presentation.handlers.userinterface_handler import UserInterfaceHandler
from presentation.menus.pause import PauseMenu
from presentation.menus.hud import HUD
from presentation.menus.upgrade_menu import UpgradeMenu
from presentation.menus.game_over import GameOver


class Display(IDisplay):
    """Class for displaying the game world."""

    def __init__(self):
        # Set the window display mode
        self.__interface_handler = UserInterfaceHandler()
        self.__screen = pygame.display.set_mode(settings.SCREEN_DIMENSION)

        # Set the window title
        pygame.display.set_caption(settings.GAME_TITLE)

        # Initialize the camera
        self.camera = Camera()

        self.__ground_tileset = self.__load_ground_tileset()
        self.__world: IGameWorld = None

    @property
    def screen(self):
        return self.__screen

    def __load_ground_tileset(self):
        return Tileset(
            "./assets/ground_tileset.png", settings.TILE_WIDTH, settings.TILE_HEIGHT, 16, 16
        )

    def __render_ground_tiles(self):
        # Calculate the range of tiles to render based on the camera position
        start_col = max(0, self.camera.camera_rect.left // settings.TILE_WIDTH)
        end_col = min(
            settings.WORLD_COLUMNS, (self.camera.camera_rect.right // settings.TILE_WIDTH) + 1
        )
        start_row = max(0, self.camera.camera_rect.top // settings.TILE_HEIGHT)
        end_row = min(
            settings.WORLD_ROWS, (self.camera.camera_rect.bottom // settings.TILE_HEIGHT) + 1
        )

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                # Get the tile index from the tile map
                tile_index = self.__world.tile_map.get(row, col)
                tile_image = self.__ground_tileset.get_tile(tile_index)

                # Calculate the position on the screen
                x = col * settings.TILE_WIDTH - self.camera.camera_rect.left
                y = row * settings.TILE_HEIGHT - self.camera.camera_rect.top

                self.__screen.blit(tile_image, (x, y))

    def __draw_player_health_bar(self):
        self.__draw_health_bar_for_entity(self.__world.player)

    def __draw_health_bar_for_entity(self, entity):
        bar_width = settings.TILE_WIDTH
        bar_height = 5
        bar_x = entity.sprite.rect.centerx - bar_width // 2 - self.camera.camera_rect.left
        bar_y = entity.sprite.rect.bottom + 3 - self.camera.camera_rect.top

        # Draw the background bar (red)
        bg_rect = pygame.Rect(bar_x - 1, bar_y - 1, bar_width + 2, bar_height + 2)
        pygame.draw.rect(self.__screen, (0, 0, 0), bg_rect)

        bg_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
        pygame.draw.rect(self.__screen, (255, 0, 0), bg_rect)

        # Draw the health bar (green)
        health_percentage = entity.health / entity.max_health
        health_width = int(bar_width * health_percentage)
        health_rect = pygame.Rect(bar_x, bar_y, health_width, bar_height)
        pygame.draw.rect(self.__screen, (0, 255, 0), health_rect)

        text_size = 15
        font_obj = pygame.font.SysFont(None, text_size)
        rendered = font_obj.render(f"{round(entity.health)} ({round(entity.health/entity.max_health * 100)}%)", True, (255, 255, 255))
        rect = rendered.get_rect(center=(bar_x + bar_width // 2, bar_y + bar_height + text_size // 2))
        self.__screen.blit(rendered, rect)

    def __draw_player(self):
        adjusted_rect = self.camera.apply(self.__world.player.sprite.rect)
        self.__screen.blit(self.__world.player.sprite.image, adjusted_rect)

        self.__draw_player_health_bar()

    def __show_interface(self):
        self.__interface_handler.update(self)

    def load_world(self, world: IGameWorld):
        self.__world = world

        self.__interface_handler.add_menu(HUD(self.__world))
        self.__interface_handler.add_menu(PauseMenu(self.__world))
        self.__interface_handler.add_menu(UpgradeMenu(self.__world))
        self.__interface_handler.add_menu(GameOver(self.__world))

    def get_menu(self, name: str):
        return self.__interface_handler.get_menu(name)

    def render_frame(self):
        # Update the camera to follow the player
        self.camera.update(self.__world.player.sprite.rect)

        # Render the ground tiles
        self.__render_ground_tiles()

        # Draw all the experience gems
        for collectible in self.__world.collectibles:
            if self.camera.camera_rect.colliderect(collectible.sprite.rect):
                adjusted_rect = self.camera.apply(collectible.sprite.rect)
                self.__screen.blit(collectible.sprite.image, adjusted_rect)

        # Draw all monsters
        for monster in self.__world.monsters:
            if self.camera.camera_rect.colliderect(monster.sprite.rect):
                adjusted_rect = self.camera.apply(monster.sprite.rect)
                self.__screen.blit(monster.sprite.image, adjusted_rect)

                if monster.can_show_hp():
                    self.__draw_health_bar_for_entity(monster)

        # Draw the bullets
        for attack in self.__world.attacks:
            if self.camera.camera_rect.colliderect(attack.sprite.rect):
                adjusted_rect = self.camera.apply(attack.sprite.rect)
                self.__screen.blit(attack.sprite.image, adjusted_rect)

        # Draw the player
        self.__draw_player()

        # Draw the user interface
        self.__show_interface()

        # Update the display
        pygame.display.flip()
