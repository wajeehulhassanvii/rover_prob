from mars_rover_world.position import Position
from mars_rover_world.plateau import Plateau
from mars_rover_world.rover import Rover


def main():
    # create plateau and position for intitial parameters
    plateau = Plateau(5, 5)
    position = Position(1, 2)
    # Create rover instance, we will later change
    # the position of the rover in the plateau
    rover = Rover(plateau, position, Rover.DIRECTIONS.get('N'))
    rover.process_command_string("LMLMLMLMM")
    # print the corrent location and direction
    print(rover)

    # change the location of the rover
    rover.set_position(3, 3, Rover.DIRECTIONS.get('E'))
    rover.process_command_string("MMRMMRMRRM")
    # print the corrent location and direction
    print(rover)


if __name__ == "__main__":
    main()
