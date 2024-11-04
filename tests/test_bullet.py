# pylint: disable=C0114,C0115,C0116
import unittest

from pygame import Vector2
from business.entities.bullet import Bullet
from tests.world_mock import GameWorldMock

class TestBullet(unittest.TestCase):
    def setUp(self):
        self.bullet = Bullet(Vector2(), Vector2(10, 10), 5)
        self.world = GameWorldMock()

    def test_initial_health(self):
        self.assertEqual(self.bullet.charges_remaining, 1)

    def test_damage_amount(self):
        self.assertEqual(self.bullet.damage, 5)

    def test_take_damage(self):
        self.bullet.use_charge()
        self.assertEqual(self.bullet.charges_remaining, 0)

    def test_update_position(self):
        x_distance, y_distance = 3, 4

        self.bullet = Bullet(Vector2(), Vector2(x_distance, y_distance), 1)
        self.bullet.update(self.world)

        x, y = self.bullet.pos.x, self.bullet.pos.y
        self.assertAlmostEqual(x, 6)
        self.assertAlmostEqual(y, 8)
        self.assertAlmostEqual(x / x_distance, y / y_distance)

    def test_update_position_vertical(self):
        x_distance, y_distance = 0, 10

        self.bullet = Bullet(Vector2(), Vector2(x_distance, y_distance), 1)
        self.bullet.update(self.world)

        x, y = self.bullet.pos.x, self.bullet.pos.y
        self.assertAlmostEqual(x, 0)
        self.assertAlmostEqual(y, 10)

    def test_update_position_horizontal(self):
        x_distance, y_distance = 10, 0

        self.bullet = Bullet(Vector2(), Vector2(x_distance, y_distance), 1)
        self.bullet.update(self.world)

        x, y = self.bullet.pos.x, self.bullet.pos.y
        self.assertAlmostEqual(x, 10)
        self.assertAlmostEqual(y, 0)

    def test_update_position_non_zero_src(self):
        src_x, src_y, dst_x, dst_y = 5, 5, 10, 10

        self.bullet = Bullet(Vector2(src_x, src_y), Vector2(dst_x, dst_y), 1)
        self.bullet.update(self.world)

        x, y = self.bullet.pos.x, self.bullet.pos.y
        self.assertAlmostEqual(x, 12.07, 2)
        self.assertAlmostEqual(y, 12.07, 2)


if __name__ == "main":
    unittest.main()
