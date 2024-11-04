"""Creates the final boss
"""

from pygame import Vector2
from business.entities.monsters.monster import Monster
from presentation.sprite import BossSprite

class Boss(Monster):
    """The boss in game"""

    def __init__(self, pos: Vector2):
        super().__init__(pos, BossSprite(pos), 80, "boss",
                         health=300,
                         damage=20,
                         range=100)
