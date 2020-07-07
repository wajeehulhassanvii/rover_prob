class Plateau:
    MIN_W = 0
    MIN_H = 0

    def __init__(self, width, height, min_w=0, min_h=0):
        # if width < 0:
        #     width = 0
        # if height < 0:
        #     height = 0
        self.width = width
        self.height = height
        self.MIN_W = min_w
        self.MIN_H = min_h

    def move_available(self, position):
        """check if whether move is available and return T/F"""
        return self.MIN_H <= position.y <= self.height and \
            self.MIN_W <= position.x <= self.width
