"""This module contains the Monster class, which represents a monster entity in the game."""

from pygame import Vector2

from business.entities.entity import MovableEntity
from business.entities.interfaces import IDamageable, IMonster
from business.handlers.cooldown_handler import CooldownHandler
from business.world.interfaces import IGameWorld
from business.world.clock import Clock
from presentation.sprite import Sprite


class Monster(MovableEntity, IMonster):
    """A monster entity in the game."""

    def __init__(self, pos: Vector2, sprite: Sprite, mov_speed: int, monster_type: str, health: int=1, damage: int=3, range: int=60):
        super().__init__(pos, mov_speed, sprite)
        clock_time = Clock().time
        health = (health + round(clock_time/20)) * max((clock_time / 180), 1)

        self.__health: int = health
        self.__max_health = health
        self.__damage = damage * (clock_time / 120)
        self.__attack_range = range
        self.__attack_cooldown = CooldownHandler(0.5)
        self.__dmg_taken_cooldown = CooldownHandler(2.5)
        self.__can_move_cooldown = CooldownHandler(mov_speed / 480)
        self.__monster_type = monster_type
        self._logger.debug("Created %s", self)

    def attack(self, target: IDamageable):
        """Attacks the target."""
        if not self.__attack_cooldown.is_action_ready():
            return

        if self.pos.distance_to(target.pos) < self.__attack_range:
            target.take_damage(self.damage)
            self.__attack_cooldown.put_on_cooldown()

    def __get_direction_towards_the_player(self, world: IGameWorld):
        direction: Vector2 = self.pos - world.player.pos
        y = direction.y * world.simulation_speed
        x = direction.x * world.simulation_speed

        if x != 0:
            x = -x // abs(x)

        if y != 0:
            y = -y // abs(y)

        return Vector2(x, y)

    def __movement_collides_with_entities(self, delta: Vector2, entities: list[IMonster], player) -> bool:
        #for entity in entities:
            #if entity == self:
             #   continue

            #if self.sprite.rect.colliderect(entity.sprite.rect) and entity.can_move:
                #other_to_plr = entity.pos.distance_to(player.pos)
                #self_to_plr = self.pos.distance_to(player.pos)

                #if other_to_plr > self_to_plr:
                    #self.__can_move_cooldown.put_on_cooldown()

                    #return Vector2(0, 0)

        return delta

    @property
    def type(self) -> str:
        return self.__monster_type

    def update(self, world: IGameWorld):
        self.attack(world.player)

        direction = self.__get_direction_towards_the_player(world)
        if direction.magnitude == 0 or not self.can_move:
            return

        if self.pos.distance_to(world.player.pos) < 25:
            return

        new_dir = self.__movement_collides_with_entities(direction, world.monsters, world.player)
        if new_dir:
            self.move(new_dir)

        if direction.x < 0:
            self.sprite.flip(True)
        elif direction.y > 0:
            self.sprite.flip(False)

        super().update(world)

    def __str__(self):
        return f"Monster(hp={self.health}, pos={self.pos.x, self.pos.y})"

    @property
    def damage(self):
        return self.__damage

    @property
    def health(self) -> int:
        return self.__health

    @property
    def can_move(self) -> bool:
        return self.__can_move_cooldown.is_action_ready()

    @property
    def max_health(self) -> int:
        return self.__max_health

    @property
    def attack_cooldown(self):
        return self.__attack_cooldown

    def take_damage(self, amount):
        self.__health = max(0, self.__health - abs(amount))
        self.__dmg_taken_cooldown.put_on_cooldown()
        self.sprite.take_damage()

    def can_show_hp(self):
        return not self.__dmg_taken_cooldown.is_action_ready()
