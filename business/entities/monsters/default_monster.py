"""Creates a default monster
"""

from pygame import Vector2
from business.entities.monsters.monster import Monster
from presentation.sprite import GhostSprite

class DefaultMonster(Monster):
    """The default monster in game"""

    def __init__(self, pos: Vector2):
        super().__init__(pos, GhostSprite(pos), 120)
