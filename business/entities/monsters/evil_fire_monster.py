"""
    Creates an evil fire monster
        (MONSTRUO DE LA DEFENSA)

"""

from pygame import Vector2
from business.entities.monsters.monster import Monster
from presentation.sprite import EvilFireMonsterSprite

class EvilFireMonster(Monster):
    """The default monster in game"""

    def __init__(self, pos: Vector2):
        super().__init__(pos, EvilFireMonsterSprite(pos), 120, "fire", 7)

        self.__shield = self.health // 2

    @property
    def shield(self):
        """The amount of shield the monster has"""

        return self.__shield

    def take_damage(self, amount):
        new_amount = amount
        if self.__shield > 0:
            new_amount -= self.shield
            self.__shield = max(0, self.__shield - amount)

            if new_amount < 0:
                return

        super().take_damage(new_amount)
