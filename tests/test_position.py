import unittest
from unittest import TestCase

from mars_rover_world.position import Position


class TestPosition(TestCase):
    """Class to test position"""

    def test_position_creation(self):
        """Test that position created is correct"""
        x = 1
        y = 0
        position = Position(x, y)
        self.assertEqual(position.x, x)
        self.assertEqual(position.y, y)

    def test_intial_position_value(self):
        """Test that the initial value of position is 0,0"""
        position = Position()
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)


if __name__ == '__main__':
    unittest.main()
