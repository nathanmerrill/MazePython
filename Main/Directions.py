import random


class Directions:
    TOP, LEFT, BOTTOM, RIGHT = range(4)

    def __init__(self, direction):
        if direction < 0 or direction >= 4:
            raise ValueError("Invalid direction")
        self.value = direction

    def __str__(self):
        return{
            Directions.TOP: "TOP",
            Directions.LEFT: "LEFT",
            Directions.BOTTOM: "BOTTOM",
            Directions.RIGHT: "RIGHT",
        }[self.value]

    def __eq__(self, other):
        if not other:
            return False
        return self.value == other.value

    def __hash__(self):
        return self.value

    def __repr__(self):
        return str(self)

    def get_opposite(self):
        return Directions((self.value+2) % 4)

    @staticmethod
    def get_all():
        return [Directions(x) for x in range(4)]

    @staticmethod
    def get_all_random(weight):
        available = Directions.get_all()
        directions = []
        while available:
            direction = Directions.get_random(weight, available)
            directions.append(direction)
            available.remove(direction)
        return directions

    @staticmethod
    def get_random(weight, available=None):
        if not available:
            available = Directions.get_all()
        random_range = 0.0
        for direction in available:
            if direction.is_horizontal():
                random_range += weight/2.0
            else:
                random_range += (1-weight)/2.0
        r = random.uniform(0, random_range)
        for direction in available:
            if direction.is_horizontal():
                r -= weight/2.0
            else:
                r -= (1-weight)/2.0
            if r < 0:
                return direction

    def is_vertical(self):
        return self.value % 2 == 0

    def is_horizontal(self):
        return self.value % 2 == 1

    def to_coordinates(self):
        return{
            Directions.TOP: (0, -1),
            Directions.LEFT: (-1, 0),
            Directions.BOTTOM: (0, 1),
            Directions.RIGHT: (1, 0),
        }[self.value]

