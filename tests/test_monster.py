#pylint: skip-file

import unittest
from unittest.mock import MagicMock, patch

from pygame import Vector2, display
from business.entities.interfaces import IDamageable
from business.entities.monsters.red_ghost import RedGhost


class TestMonster(unittest.TestCase):
    def setUp(self):
        display.set_mode((100, 100))

        self.monster = RedGhost(Vector2(5, 5))

    def test_attack(self):
        target_mock = MagicMock(spec=IDamageable)
        target_mock.pos = Vector2()
        target_mock.health = 10

        with patch.object(
            self.monster.attack_cooldown,  # pylint: disable=W0212
            "is_action_ready",
            return_value=True,
        ):
            self.monster.attack(target_mock)

        target_mock.take_damage.assert_called_once_with(self.monster.damage)

    def test_attack_is_not_called_when_action_is_not_ready(self):
        target_mock = MagicMock(spec=IDamageable)
        target_mock.health = 10

        with patch.object(
            self.monster.attack_cooldown,  # pylint: disable=W0212
            "is_action_ready",
            return_value=False,
        ):
            self.monster.attack(target_mock)

        target_mock.take_damage.assert_not_called()
