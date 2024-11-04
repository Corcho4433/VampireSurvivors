#pylint: skip-file

from pygame import Vector2, display
import unittest

from business.entities.player import Player
from business.progression.inventory import Inventory
from business.entities.monsters.default_monster import DefaultMonster
from business.weapons.weapon_factory import WeaponFactory
from tests.world_mock import GameWorldMock

class TestsItemDataHandler(unittest.TestCase):
    def setUp(self):
        display.set_mode((0, 0))

        self.world = GameWorldMock()
        self.player = Player(Vector2(), 1, 0)
        self.monster = DefaultMonster(Vector2(2, 2))
        self.world.add_monster(self.monster)
    
    def test01_player_obtains_whip_and_kills_enemy(self):
        new_whip = WeaponFactory.create_weapon('whip')
        new_whip.cooldown_handler.change_time(0)
        new_whip.cooldown_handler.put_on_cooldown()

        self.player.assign_inventory(Inventory())

        self.player.give_item(new_whip)
        for weapon in self.player.inventory.get_weapons():
            weapon.attack(self.player.pos, self.world, self.player.stats)

        for attack in self.world.attacks:
            attack.update(self.world)
        
        self.assertEqual(self.player.inventory.get_weapons(), [new_whip])
        self.assertEqual(self.monster.health, 0)
        self.assertEqual(self.world.total_damage, 3)
        self.assertEqual(self.player.inventory.get_items(), [new_whip])

if __name__ == "__main__":
    unittest.main()