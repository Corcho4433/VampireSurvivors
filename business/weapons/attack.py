import pygame

from business.weapons.interfaces import IAttack
from business.weapons.hitbox import Hitbox
from business.world.interfaces import IGameWorld
from presentation.sprite import AttackSprite
from presentation.sprite import Sprite

class Attack(IAttack):
    def __init__(self, pos: pygame.Vector2, damage: int):
        self.__sprite : Sprite = AttackSprite(pos)
        self.__damage = damage
        self.__hitbox : Hitbox = Hitbox(pygame.Vector2(100,100), pos)

    def 

    @property
    def damage(self):
        return self.__damage
