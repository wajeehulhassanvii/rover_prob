import unittest
from unittest import TestCase

from mars_rover_world.rover import Rover
from mars_rover_world.position import Position
from mars_rover_world.plateau import Plateau


class TestRover(TestCase):
    """Class for testing rover"""

    def test_rover_creation(self):
        """test that rover has been successfully created"""
        plateau = Plateau(5, 5)
        position = Position(3, 3)

        rover = Rover(plateau, position, Rover.DIRECTIONS['W'])

        self.assertEqual(Position(3, 3), rover.position)
        self.assertEqual(plateau, rover.plateau)

    def test_rover_movement(self):
        """test whether the rover can move or not"""
        plateau = Plateau(4, 4)
        position = Position(3, 3)

        rover1 = Rover(plateau, position, Rover.DIRECTIONS['N'])  # y + 1
        rover2 = Rover(plateau, position, Rover.DIRECTIONS['E'])  # x + 1
        rover3 = Rover(plateau, position, Rover.DIRECTIONS['S'])  # y - 1
        rover4 = Rover(plateau, position, Rover.DIRECTIONS['W'])  # x - 1

        self.assertEqual(rover1.move(), True)
        self.assertEqual(rover2.move(), True)
        self.assertEqual(rover3.move(), True)
        self.assertEqual(rover4.move(), True)
        # position inside the rover hasn't changed, should change
        rover1.move()
        self.assertEqual(rover1.position, Position(3, 4))

    def test_multiple_rovers(self):
        """test multiple rovers moving on the plateau"""
        pass

    def test_rover_directions(self):
        """test whether the directions of the rover"""
        self.assertEqual(Rover.DIRECTIONS['N'], 1)
        self.assertEqual(Rover.DIRECTIONS['E'], 2)
        self.assertEqual(Rover.DIRECTIONS['S'], 3)
        self.assertEqual(Rover.DIRECTIONS['W'], 4)

    def test_set_position_function(self):
        """test that the set_position func is working properly"""
        plateau = Plateau(4, 4)
        position = Position(3, 3)

        rover = Rover(plateau, position, Rover.DIRECTIONS['N'])
        rover.set_position(3, 3, Rover.DIRECTIONS["E"])
        self.assertEqual(str(rover), "3 3 E")
        rover.set_position(2, 2, Rover.DIRECTIONS["W"])
        self.assertEqual(str(rover), "2 2 W")

    def test_turn_left_function(self):
        """test the turn left function"""
        plateau = Plateau(4, 4)
        position = Position(3, 3)

        rover = Rover(plateau, position, Rover.DIRECTIONS['N'])
        rover.turn_left()
        self.assertEqual(str(rover), "3 3 W")

    def test_turn_right_function(self):
        """test the turn right function"""
        plateau = Plateau(4, 4)
        position = Position(3, 3)

        rover = Rover(plateau, position, Rover.DIRECTIONS['N'])
        rover.turn_right()
        self.assertEqual(str(rover), "3 3 E")


if __name__ == '__main__':
    unittest.main()
