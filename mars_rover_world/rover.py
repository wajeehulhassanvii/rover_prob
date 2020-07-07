from mars_rover_world.position import Position


class Rover(object):

    DIRECTIONS = {
        "N": 1,
        "E": 2,
        "S": 3,
        "W": 4
    }

    heading = DIRECTIONS["N"]

    def __init__(self, plateau, position, heading):
        """initialize rover with the parameters"""
        self.plateau = plateau
        self.position = position
        self.heading = heading

    def set_position(self, x, y, heading):
        if not isinstance(self.position, Position):
            self.position = Position(x, y)
        else:
            self.position.x = x
            self.position.y = y
        self.heading = heading

    @property
    def get_heading(self):
        directions = list(self.DIRECTIONS.keys())
        try:
            direction = directions[self.heading - 1]
        except IndexError:
            direction = "N"
            print("Direction error...")
        return direction

    @property
    def current_position(self):
        return "{} {} {}".format(self.position.x,
                                 self.position.y,
                                 self.get_heading)

    def __str__(self):
        return self.current_position

    def move(self):
        if not self.plateau.move_available(self.position):
            return False

        # According to condition given square
        # directly North from (x, y) is (x, y+1)
        if self.DIRECTIONS["N"] == self.heading:
            self.position.y += 1
        elif self.DIRECTIONS["E"] == self.heading:
            self.position.x += 1
        elif self.DIRECTIONS["S"] == self.heading:
            self.position.y -= 1
        elif self.DIRECTIONS["W"] == self.heading:
            self.position.x -= 1

        return True

    def turn_left(self):
        self.heading = self.DIRECTIONS["W"] if (self.heading - 1)\
            < self.DIRECTIONS["N"] else (self.heading - 1)

    def turn_right(self):
        self.heading = self.DIRECTIONS["N"] if (self.heading + 1)\
             > self.DIRECTIONS["W"] else (self.heading + 1)

    def execute_single_command(self, command):
        if 'L' == command:
            self.turn_left()
        elif 'R' == command:
            self.turn_right
        elif 'M' == command:
            if not self.move():
                print("You can't go there, sorry")
        else:  # unrecognized command
            print("I am not programmed to do this!")

    def process_command_string(self, commands):
        for i in range(len(commands)):
            self.execute_single_command(commands[i])
