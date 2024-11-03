import pygame

from business.weapons.interfaces import IAttack
from business.weapons.hitbox import Hitbox
from business.world.interfaces import IGameWorld
from business.entities.interfaces import IMonster
from business.entities.entity import Entity
from presentation.sprite import AttackSprite
from presentation.sprite import Sprite

class Attack(Entity, IAttack):
    """An attack for a weapon"""

    def __init__(self, pos: pygame.Vector2, damage: int):
        super().__init__(pos, AttackSprite(pos))
        self.__damage = damage
        self.__hitbox : Hitbox = Hitbox(pygame.Vector2(100,100), pos)
        self.__finished : bool = False
        self.__damaged_monsters : list[IMonster] = []

    def __deal_damage(self, world: IGameWorld):
        monsters = self.__hitbox.get_enemies_inside(world)
        for monster in monsters:
            monster.take_damage(self.damage)
        self.__damaged_monsters.append(monsters)
        self.__finished = True

    def update(self, world):
        self.__deal_damage(world)
        super().update(world)

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
