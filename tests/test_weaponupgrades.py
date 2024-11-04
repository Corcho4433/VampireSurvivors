#pylint: skip-file

import unittest

from business.handlers.data_handler import DataHandler
from business.weapons.weapon_factory import WeaponFactory
from business.exceptions import InvalidWeaponName

class TestsWeaponUpgrades(unittest.TestCase):
    def test01_wrong_weapon_raises_error(self):
        with self.assertRaises(InvalidWeaponName):
            WeaponFactory.create_weapon('vater_boiler_skibidi_master')

    def test02_weapon_type_is_weapon(self):
        gun = WeaponFactory.create_weapon('gun')
        
        self.assertEqual(1, gun.item_type)

    def test03_weapon_can_level_up(self):
        gun = WeaponFactory.create_weapon('gun')
        gun.upgrade()

        self.assertEqual(2, gun.level)

    def test04_gun_stats_are_correct(self):
        gun = WeaponFactory.create_weapon('gun')

        self.assertEqual(1, gun.speed)

    def test05_gun_stats_on_level_up_are_correct(self):
        gun = WeaponFactory.create_weapon('gun')
        gun.upgrade()

        self.assertEqual(1.3, gun.speed)

    def test06_gun_damage_changed(self):
        gun = WeaponFactory.create_weapon('gun')
        gun.change_stat('damage', 500)

        self.assertEqual(500, gun.damage)