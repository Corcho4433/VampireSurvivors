"""Player entity module."""

import pygame
import settings

from business.handlers.cooldown_handler import CooldownHandler
from business.entities.entity import MovableEntity
from business.entities.experience_gem import ExperienceGem
from business.entities.interfaces import ICanDealDamage, IDamageable, IPlayer
from business.world.interfaces import IGameWorld
from business.progression.inventory import Inventory
from business.progression.player_stats import PlayerStats
from presentation.sprite import Sprite
from business.progression.interfaces import IInventoryItem

class Player(MovableEntity, IPlayer, IDamageable, ICanDealDamage):
    """Player entity.

        The player is the main character of the game. 
        It can move around the game world and shoot at monsters.
    """

    def __init__(self, pos: pygame.Vector2, sprite: Sprite):
        super().__init__(pos, 300, sprite)

        self.__stats = PlayerStats(health=100)
        self.__last_shot_time = CooldownHandler(self.__stats.cooldown)
        self.__world: IGameWorld = None
        self.__inventory : Inventory = None
        self.__experience = 0
        self.__max_health = self.__stats.health
        self.__level = 1
        self._logger.debug("Created %s", self)

    def __assign_inventory(self):
        self.__inventory = Inventory(self.__world)

    def __str__(self):
        return f"Player(hp={self.__stats.health}, xp={self.__experience}, lvl={self.__level}, pos=({self._pos.x}, {self._pos.y}))" #pylint: disable=C0301

    @property
    def experience(self):
        return self.__experience

    @property
    def inventory(self):
        return self.__inventory

    @property
    def experience_to_next_level(self):
        return round(self.__level ** settings.EXPERIENCE_PER_LEVEL_RATIO)

    @property
    def level(self):
        return self.__level

    @property
    def damage(self):
        return self.__stats.attack_damage

    @property
    def luck(self):
        return self.__stats.luck

    @property
    def health(self) -> int:
        #print(self.__stats.health)
        return self.__stats.health
    
    @property
    def max_health(self) -> int:
        return self.__max_health

    @property
    def stats(self) -> PlayerStats:
        return self.__stats

    def upgrade_item(self, item: IInventoryItem):
        for inventory_item in self.__inventory.get_weapons():
            if inventory_item == item:
                inventory_item.upgrade()

    def take_damage(self, amount):
        self.__stats.health = max(0, self.__stats.health - amount)

        self.sprite.take_damage()

    def pickup_gem(self, gem: ExperienceGem):
        self.__gain_experience(gem.amount)

    def __gain_experience(self, amount: int):
        self.__experience += amount
        while self.__experience >= self.experience_to_next_level:
            self.__experience -= self.experience_to_next_level
            self.__level += 1
            self.__world.set_upgrade_menu_active(True)

    def __attack_at_nearest_enemy(self, world: IGameWorld):
        for weapon in self.__inventory.get_weapons():
            weapon.attack(self.pos, world)

    def apply_perks(self):
        self.__stats = PlayerStats(health=100)

        perks = self.__inventory.get_perks()
        for perk in perks:
            self.__stats = self.__stats * perk.stats

        self.__max_health = self.__stats.health

    def assign_world(self, world: IGameWorld):
        self.__world = world
        self.__assign_inventory()
        self.apply_perks()

    def give_item(self, item: IInventoryItem):
        self.__inventory.add_item(item)

    def update(self, world: IGameWorld):
        super().update(world)

        if self.__last_shot_time.is_action_ready() and world.simulation_speed > 0:
            self.__attack_at_nearest_enemy(world)
            self.__last_shot_time.put_on_cooldown()
