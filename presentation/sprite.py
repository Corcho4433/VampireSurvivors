"""Module for the Sprite class."""

import pygame

import settings
from presentation.tileset import Tileset

def mask_to_surface(mask, color=(255, 0, 0), alpha=100):
    # Create a new surface matching the mask's size
    mask_surface = pygame.Surface(mask.get_size(), pygame.SRCALPHA)
    mask_surface.fill((0, 0, 0, 0))  # Start with a fully transparent surface

    # Fill the surface where the mask is active
    for x in range(mask.get_size()[0]):
        for y in range(mask.get_size()[1]):
            if mask.get_at((x, y)):
                mask_surface.set_at((x, y), (*color, alpha))  # Use the specified color and transparency

    return mask_surface

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
        self.__mask = pygame.mask.from_surface(self.__original_image, threshold=0)

    @property
    def mask(self):
        """The mask of the sprite"""

        return self.__mask

    @property
    def time_per_frame(self):
        """The time until the next frame in the animation"""
        return 10

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

    @property
    def size(self) -> pygame.Vector2:
        """The size of the sprite
        
            Returns:
                pygame.Vector2: The size of the sprite. A Vector2 is a vector with 2 axis
        """

        return pygame.Vector2(self._rect.width, self._rect.height)

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
        self.__next_frame_time = self.time_per_frame

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

    ASSET = "./assets/ghost.png"

    def __init__(self, pos: pygame.Vector2):
        image: pygame.Surface = pygame.image.load(GhostSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, (64,64))
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

class RedGhostSprite(Sprite):
    """A class representing the red ghost sprite."""

    ASSET = "./assets/red_ghost.png"

    def __init__(self, pos: pygame.Vector2):
        image: pygame.Surface = pygame.image.load(RedGhostSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, (64,64))
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

class EvilFireMonsterSprite(Sprite):
    """A class representing the evil fire monster"""

    ASSET = "./assets/monster_defensa.png"

    def __init__(self, pos: pygame.Vector2):
        image: pygame.Surface = pygame.image.load(EvilFireMonsterSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, (64,64))
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

class BossSprite(Sprite):
    """A class representing the player sprite."""

    ASSET = "./assets/boss.png"

    def __init__(self, pos: pygame.Vector2):
        self.__moving_tileset = Tileset(
            BossSprite.ASSET, settings.TILE_HEIGHT * 3, settings.TILE_HEIGHT * 3, 4, 2
        )
        self.__current_tile = 7

        image: pygame.Surface = self.__moving_tileset.get_tile(self.__current_tile)
        rect: pygame.Rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

    def advance_frame(self):
        if self.time_until_next_frame > 0:
            return

        if self.__current_tile - 1 < 0:
            self.__current_tile = 7
        else:
            self.__current_tile -= 1

        super().advance_frame()

        if self.state == 'moving':
            self._image = self.__moving_tileset.get_tile(self.__current_tile)
        elif self.state == 'idle':
            self._image = self.__moving_tileset.get_tile(0)

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

    ASSET = "./assets/whip_attack_spritesheet.png"

    def __init__(self, pos: pygame.Vector2, scale: int):
        self.__moving_tileset = Tileset(
            AttackWhipSprite.ASSET, round(200 * scale), round(200 * scale), 4, 4
        )
        self.__current_tile = 0

        image: pygame.Surface = self.__moving_tileset.get_tile(self.__current_tile)
        rect: pygame.Rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

    def advance_frame(self):
        if self.time_until_next_frame > 0:
            return

        if self.__current_tile + 1 > 15:
            self.__current_tile = 0
        else:
            self.__current_tile += 1

        super().advance_frame()

        self._image = self.__moving_tileset.get_tile(self.__current_tile)

    @property
    def time_per_frame(self):
        return 1

class ExperienceGemSprite(Sprite):
    """A class representing the experience gem sprite."""

    ASSET = "./assets/experience_gem.png"

    def __init__(self, pos: pygame.Vector2):
        image: pygame.Surface = pygame.image.load(ExperienceGemSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, (32,32))
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

class HealingGemSprite(Sprite):
    """A class representing the healing gem sprite."""

    ASSET = "./assets/healing_gem.png"

    def __init__(self, pos: pygame.Vector2):
        image: pygame.Surface = pygame.image.load(HealingGemSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, (32,32))
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)

class ChaoticGemSprite(Sprite):
    """A class representing the chaotic gem sprite."""

    ASSET = "./assets/chaos_gem.png"

    def __init__(self, pos: pygame.Vector2):
        image: pygame.Surface = pygame.image.load(ChaoticGemSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, (32,32))
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)


class ChestSprite(Sprite):
    """A class representing the chest sprite."""

    ASSET = "./assets/chest.png"

    def __init__(self, pos: pygame.Vector2):
        image: pygame.Surface = pygame.image.load(ChestSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, (32,32))
        rect: pygame.rect = image.get_rect(center=(int(pos.x), int(pos.y)))

        super().__init__(image, rect)
