import unittest
from unittest import TestCase

from mars_rover_world.plateau import Plateau
from mars_rover_world.position import Position


class TestPlateau(TestCase):
    """Test Plateau class here"""

    def test_minimum_width(self):
        """"""
        plateau = Plateau(1, 1)
        self.assertEqual(plateau.MIN_W, 0)
        self.assertEqual(plateau.MIN_H, 0)

    def test_plateau_creation(self):
        """Test that Plateau created with right value"""
        plateau1 = Plateau(6, 8)
        plateau2 = Plateau(4, 10)

        self.assertEqual(plateau1.width, 6)
        self.assertEqual(plateau1.height, 8)
        self.assertEqual(plateau2.width, 4)
        self.assertEqual(plateau2.height, 10)

    def test_plateau_non_negative(self):
        """Test that plateau creation is non negative"""
        plateau = Plateau(-1, -10)

        self.assertGreaterEqual(plateau.width, 0)
        self.assertGreaterEqual(plateau.height, 0)

    def test_move_availibility(self):
        """Test if move is available"""
        plateau = Plateau(5, 5)

        position_1 = Position(5, 6)
        position_2 = Position(3, 3)
        position_3 = Position(-1, 0)

        is_move_available_1 = plateau.move_available(position_1)
        is_move_available_2 = plateau.move_available(position_2)
        is_move_available_3 = plateau.move_available(position_3)

        self.assertEqual(is_move_available_1, False)
        self.assertEqual(is_move_available_2, True)
        self.assertEqual(is_move_available_3, False)


if __name__ == '__main__':
    unittest.main()
