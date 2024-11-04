"""Player entity module."""

import pygame
import settings

from business.handlers.cooldown_handler import CooldownHandler
from business.entities.entity import MovableEntity
from business.entities.interfaces import ICanDealDamage, IDamageable, IPlayer
from business.world.interfaces import IGameWorld
from business.progression.inventory import Inventory
from business.progression.player_stats import PlayerStats
from business.progression.interfaces import IInventoryItem
from business.handlers.position_handler import PositionHandler
from presentation.sprite import PlayerSprite

class Player(MovableEntity, IPlayer, IDamageable, ICanDealDamage):
    """Player entity.

        The player is the main character of the game. 
        It can move around the game world and shoot at monsters.
    """

    def __init__(self, pos: pygame.Vector2, level=1, experience=0):
        super().__init__(pos, 300, PlayerSprite(pos))

        self.__stats = PlayerStats(health=100)
        self.__last_shot_time = CooldownHandler(self.__stats.cooldown)
        self.__world: IGameWorld = None
        self.__inventory : Inventory = None
        self.__experience = experience
        self.__max_health = self.__stats.health
        self.__level = level
        self._logger.debug("Created %s", self)

    def assign_inventory(self, inventory):
        self.__inventory = inventory

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

    def pickup_gem(self, gem):
        self.__gain_experience(gem.amount)

    def __gain_experience(self, amount: int):
        self.__experience += amount
        while self.__experience >= self.experience_to_next_level:
            self.__experience -= self.experience_to_next_level
            self.__level += 1
            self.__world.set_upgrade_menu_active(True)

    def __attack_at_nearest_enemy(self, world: IGameWorld):
        for weapon in self.__inventory.get_weapons():
            weapon.attack(self.pos, world, self.stats)

    def apply_perks(self, heal: bool):
        current_health = self.__stats.health
        self.__stats = PlayerStats(health=100)

        perks = self.__inventory.get_perks()
        for perk in perks:
            self.__stats = self.__stats * perk.stats

        self.__max_health = self.__stats.health
        if not heal:
            self.__stats.health = current_health

    def assign_world(self, world: IGameWorld):
        self.__world = world
        self.apply_perks(heal=True)

    def give_item(self, item: IInventoryItem):
        self.__inventory.add_item(item)

    def update(self, world: IGameWorld):
        super().update(world)

        if not PositionHandler.is_position_within_boundaries(self.pos):
            self.move_to_center()

        if self.__last_shot_time.is_action_ready() and world.simulation_speed > 0:
            self.__attack_at_nearest_enemy(world)
            self.__last_shot_time.put_on_cooldown()
