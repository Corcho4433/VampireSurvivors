"""
    Define the class AttackWhip, a melee attack used by the class Whip
"""

import pygame
from settings import FPS

from business.entities.interfaces import IMeleeAttack
from business.weapons.hitbox import Hitbox
from business.world.interfaces import IGameWorld
from business.entities.interfaces import IMonster
from business.entities.entity import Entity
from presentation.sprite import AttackWhipSprite

class AttackWhip(Entity, IMeleeAttack):
    """An attack for a weapon"""

    def __init__(self, pos: pygame.Vector2, damage: int, scale: int=1):
        sprite = AttackWhipSprite(pos, scale)

        super().__init__(pos, sprite)
        self.__damage = damage
        self.__hitbox: Hitbox = Hitbox(sprite.size, pos)
        self.__finished: bool = False
        self.__damaged_monsters : list[IMonster] = []
        self.__max_sprite_time = .25
        self.__current_sprite_time = 0

    def process_attack(self, world: IGameWorld):
        monsters = self.__hitbox.get_enemies_inside(world)
        for monster in monsters:
            if monster not in self.__damaged_monsters:
                self.__damaged_monsters.append(monster)
                monster.take_damage(self.damage)
                world.add_damage(self.damage)

    def update(self, world):
        super().update(world)
        self.process_attack(world)
        self._sprite.advance_frame()
        self.__current_sprite_time += 1 / FPS

        if self.__current_sprite_time > self.__max_sprite_time:
            self.__finished = True

    def __str__(self):
        return f"Melee attack(pos=({self._pos.x, self._pos.y})"

    @property
    def damage(self):
        return self.__damage

    @property
    def is_finished(self):
        return self.__finished

    @property
    def damaged_monsters(self):
        return self.__damaged_monsters
