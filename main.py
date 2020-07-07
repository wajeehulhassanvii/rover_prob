from mars_rover_world.plateau import Plateau
from mars_rover_world.position import Position
from mars_rover_world.rover import Rover


def main():
    plateau = Plateau(5, 5)
    position = Position(1, 2)
    # create rover instance
    rover = Rover(plateau, position, Rover.DIRECTIONS["N"])
    rover.process_command_string("LMLMLMLMM")
    print(rover)

    rover.set_position(3, 3, Rover.DIRECTIONS["E"])
    rover.process_command_string("MMRMMRMRRM")
    print(rover)


if __name__ == "__main__":
    main()
