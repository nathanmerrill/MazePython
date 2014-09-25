from Directions import Directions
import Utils


class Cell:
    def __init__(self, x, y, grid):
        self.coordinates = x, y
        self.open = False
        self.active = False
        self.grid = grid
        self.walls = dict(zip(Directions.get_all(), [True for _ in Directions.get_all()]))

    def __str__(self):
        string = ""
        if self.walls[1]:
            string += "|"
        else:
            string += " "
        if self.walls[0] and self.walls[2]:
            string += "="
        elif self.walls[0]:
            string += "-"
        elif self.walls[2]:
            string += "_"
        else:
            string += " "
        if self.walls[3]:
            string += "|"
        else:
            string += " "
        return string

    def has_wall(self, direction):
        return self.walls[direction]

    def get_neighbor(self, direction):
        return self.grid.get(Utils.add_tuples(self.coordinates, direction.to_coordinates()))

    def get_neighbors(self):
        return [(self.get_neighbor(i), i) for i in Directions.get_all() if self.get_neighbor(i)]

    def get_open_neighbors(self, available=None):
        if available is []:
            return []
        if not available:
            available = self.get_neighbors()
        return [i for i in available if i[0].open]

    def get_closed_neighbors(self, available=None):
        if available is []:
            return []
        if not available:
            available = self.get_neighbors()
        return [i for i in available if not i[0].open]

    def get_random_neighbor(self, weight):
        neighbors = self.get_random_neighbors(weight)
        if not neighbors:
            return None, None
        else:
            return neighbors[0]

    def get_random_neighbors(self, weight):
        return [(self.get_neighbor(i), i) for i in Directions.get_all_random(weight) if self.get_neighbor(i)]

    def get_random_open_neighbor(self, weight):
        neighbors = self.get_random_open_neighbors(weight)
        if not neighbors:
            return None, None
        return neighbors[0]

    def get_random_open_neighbors(self, weight):
        return self.get_open_neighbors(self.get_random_neighbors(weight))

    def get_random_closed_neighbor(self, weight):
        neighbors = self.get_random_closed_neighbors(weight)
        if not neighbors:
            return None, None
        return neighbors[0]

    def get_random_closed_neighbors(self, weight):
        return self.get_closed_neighbors(self.get_random_neighbors(weight))

    def is_open_neighbor(self, cell):
        for i in xrange(4):
            if cell.coordinates == self.get_neighbors()[i][0].coordinates:
                if not self.walls[i]:
                    return True
                return False
        return False

    def get_neighbor_direction(self, cell):
        for neighbor, direction in self.get_neighbors():
            if cell.coordinates == neighbor.coordinates:
                return direction

    def connect_to_cell(self, direction):
        neighbor = self.get_neighbor(direction)
        self.walls[direction] = False
        neighbor.walls[direction.get_opposite()] = False
        self.open = True
        neighbor.open = True
        self.grid.draw([self, neighbor])

    def disconnect_from_cell(self, direction):
        neighbor = self.get_neighbor(direction)
        self.walls[direction] = True
        neighbor.walls[direction.get_opposite()] = True
        if all(x is True for x in self.walls):
            self.open = False
        if all(x is True for x in neighbor.walls):
            neighbor.open = False
        self.grid.draw([self, neighbor])

    def get_connected_neighbors(self, available=None):
        if available is []:
            return []
        if not available:
            available = self.get_neighbors()
        return [i for i in available if not self.walls[i[1]]]