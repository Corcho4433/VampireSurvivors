"""Player entity module."""

import pygame

from business.entities.bullet import Bullet
from business.entities.entity import MovableEntity
from business.entities.experience_gem import ExperienceGem
from business.entities.interfaces import ICanDealDamage, IDamageable, IPlayer
from business.world.interfaces import IGameWorld
from presentation.sprite import Sprite


class Player(MovableEntity, IPlayer, IDamageable, ICanDealDamage):
    """Player entity.

    The player is the main character of the game. It can move around the game world and shoot at monsters.
    """

    BASE_DAMAGE = 5
    BASE_SHOOT_COOLDOWN = 0

    def __init__(self, pos: pygame.Vector2, sprite: Sprite):
        super().__init__(pos, 5, sprite)

        self.__health: int = 100
        self.__last_shot_time = pygame.time.get_ticks()
        self.__experience = 0
        self.__level = 1
        self._logger.debug("Created %s", self)

    def __str__(self):
        return f"Player(hp={self.__health}, xp={self.__experience}, lvl={self.__level}, pos=({self._pos.x}, {self._pos.y}))"

    @property
    def experience(self):
        return self.__experience

    @property
    def experience_to_next_level(self):
        return 1

    @property
    def level(self):
        return self.__level

    @property
    def damage_amount(self):
        return Player.BASE_DAMAGE

    @property
    def health(self) -> int:
        return self.__health

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)
        self.sprite.take_damage()

    def pickup_gem(self, gem: ExperienceGem):
        self.__gain_experience(gem.amount)

    def __gain_experience(self, amount: int):
        self.__experience += amount
        while self.__experience >= self.experience_to_next_level:
            self.__experience -= self.experience_to_next_level
            self.__level += 1

    def __shoot_at_nearest_enemy(self, world: IGameWorld):
        if not world.monsters:
            return  # No monsters to shoot at

        # Find the nearest monster
        monster = min(
            world.monsters,
            key=lambda monster: (monster.pos.distance_to(self.pos)),
        )

        # Create a bullet towards the nearest monster
        bullet = Bullet(self.pos, monster.pos, 10)
        world.add_bullet(bullet)

    @property
    def __shoot_cooldown(self):
        return Player.BASE_SHOOT_COOLDOWN

    def update(self, world: IGameWorld):
        super().update(world)

        current_time = pygame.time.get_ticks()
        if current_time - self.__last_shot_time >= self.__shoot_cooldown:
            self.__shoot_at_nearest_enemy(world)
            self.__last_shot_time = current_time