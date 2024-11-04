#pylint: skip-file

import unittest

from business.handlers.item_data_handler import ItemDataHandler
from business.progression.upgrade import Upgrade, UpgradeValue

class TestsItemDataHandler(unittest.TestCase):
    def test01_get_all_items(self):
        item_data = ItemDataHandler.get_all_items()

        self.assertEqual([('gun', 1),
                          ('whip', 1), 
                          ('hollow_heart', 2),
                          ('spinach', 2),
                          ('clover', 2),
                          ('wings', 2),
                        ], item_data)

    def test02_perk_object_is_perk_type(self):
        data = ItemDataHandler.get_item_type('clover')

        self.assertEqual(2, data)

    def test03_weapon_object_is_weapon_type(self):
        data = ItemDataHandler.get_item_type('whip')

        self.assertEqual(1, data)
    
    def test04_item_has_the_correct_upgrades(self):
        data = ItemDataHandler.get_item_upgrades('clover')

        self.assertEqual([{
            "description": "Increase the players luck by 10%",
            "repeats":5,
            "values": [
                {"type":2, "stat":"luck", "value":10}
            ]
        }], data)

if __name__ == "__main__":
    unittest.main()