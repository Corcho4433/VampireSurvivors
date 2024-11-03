"""Module for the Sprite class."""

import pygame

import settings
from presentation.tileset import Tileset


class Sprite(pygame.sprite.Sprite):
    """A class representing a sprite."""

    def __init__(self, image: pygame.Surface, rect: pygame.Rect, *groups):
        self._image: pygame.Surface = image
        self._rect: pygame.Rect = rect
        super().__init__(*groups)
        self.__flipped = False
        self.__is_in_damage_countdown = 0
        self.__next_frame_time = 0
        self.__sprite_state = "idle"
        self.__original_image: pygame.Surface = image

    @property
    def image(self) -> pygame.Surface:
        """The image of the sprite.

        Returns:
            pygame.Surface: The image of the sprite.
        """

        if self.__flipped:
            return pygame.transform.flip(self._image, True, False)

        return self._image

    @property
    def rect(self) -> pygame.Rect:
        """The rect of the sprite.

        Returns:
            pygame.Rect: The rect of the sprite. A rect is a rectangle that defines the position and size of the sprite.
        """
        return self._rect

    def update_pos(self, pos: pygame.Vector2):
        """Update the position of the sprite.

        Args:
            pos (Vector2): The coordinates of the sprite 
        """
        self._rect.center = (int(pos.x), int(pos.y))

    def flip(self, state: bool):
        """Changes the flipped state of the sprite, if true, the sprite will look the other way"""

        self.__flipped = state

    def __restore_image(self):
        self._image = self.__original_image.copy()

    def __change_color(self, color: tuple[int, int, int]):
        self._image = self.__original_image.copy()  # Make a copy of the original image
        self._image.fill(color, special_flags=pygame.BLEND_MULT)  # Change color pylint: disable=E1101
        self._image.set_colorkey((0, 0, 0))  # Set transparency if necessary

    def __decrease_damage_countdown(self):
        self.__is_in_damage_countdown -= 1
        if self.__is_in_damage_countdown <= 0:
            self.__is_in_damage_countdown = 0
            self.__restore_image()

    def take_damage(self):
        """Take damage."""
        self.__change_color((255, 0, 0))
        self.__is_in_damage_countdown = 30

    def update(self, *args, **kwargs):
        """Update the sprite behavior"""
        self.__next_frame_time -= 1
        super().__init__(*args, **kwargs)
        if self.__is_in_damage_countdown > 0:
            self.__decrease_damage_countdown()

    @property
    def time_until_next_frame(self):
        """The time until the next frame of the animation can be shown"""

        return self.__next_frame_time

    def advance_frame(self):
        """Go forward one frame in the sprite's animation"""
        self.__next_frame_time = 10

    def set_sprite_state(self, state: str):
        """Switches the sprite's state
        
            Args:
                state (str): "moving", "idle", "attack"
        """

        self.__sprite_state = state

    @property
    def state(self):
        """The sprite's current state:
         
            Returns:
                str: "moving", "idle", "attack"  
        """

        return self.__sprite_state


class PlayerSprite(Sprite):
    """A class representing the player sprite."""

    ASSET = "./assets/character.png"

    def __init__(self, pos: pygame.Vector2):
        self.__moving_tileset = Tileset(
            PlayerSprite.ASSET, settings.TILE_HEIGHT, settings.TILE_HEIGHT, 4, 1
        )
        self.__current_tile = 0

        image: pygame.Surface = self.__moving_tileset.get_tile(0)
        rect: pygame.Rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

    def advance_frame(self):
        if self.time_until_next_frame > 0:
            return

        if self.__current_tile + 1 > 3:
            self.__current_tile = 0
        else:
            self.__current_tile += 1

        super().advance_frame()

        if self.state == 'moving':
            self._image = self.__moving_tileset.get_tile(self.__current_tile)
        elif self.state == 'idle':
            self._image = self.__moving_tileset.get_tile(0)

class GhostSprite(Sprite):
    """A class representing the monster sprite."""

    ASSET = "./assets/monster.png"

    def __init__(self, pos: pygame.Vector2):
        image: pygame.Surface = pygame.image.load(GhostSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, (128,128))
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

class BulletSprite(Sprite):
    """A class representing the bullet sprite."""

    def __init__(self, pos: pygame.Vector2):
        size = 15

        image = pygame.Surface((size, size), pygame.SRCALPHA)  # pylint: disable=E1101
        pygame.draw.circle(image, (255, 255, 0), (size // 2, size // 2), size // 2)
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

class AttackWhipSprite(Sprite):
    """A class representing the melee attack sprite."""

    def __init__(self, pos: pygame.Vector2):
        size = 48

        image = pygame.Surface((size, size), pygame.SRCALPHA)  # pylint: disable=E1101
        pygame.draw.circle(image, (255, 0, 0), (size // 2, size // 2), size // 2)
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

class ExperienceGemSprite(Sprite):
    """A class representing the experience gem sprite."""

    ASSET = "./assets/experience_gem.png"

    def __init__(self, pos: pygame.Vector2):
        image: pygame.Surface = pygame.image.load(ExperienceGemSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, (32,32))
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)
