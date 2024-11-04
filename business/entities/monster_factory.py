"""Defines the monster factory that creates all kinds of monsters"""

from pygame import Vector2
from business.entities.monsters.default_monster import DefaultMonster
from business.entities.monsters.red_ghost import RedGhost
from business.entities.monsters.boss import Boss
from business.entities.interfaces import IMonsterFactory

class MonsterFactory(IMonsterFactory):
    """Creates monsters for the world"""

    @staticmethod
    def create_monster(monster_type: str, pos: Vector2):
        match monster_type:
            case "default":
                return DefaultMonster(pos)
            case "red_ghost":
                return RedGhost(pos)
            case "boss":
                return Boss(pos)
