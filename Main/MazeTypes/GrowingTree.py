import random


class GrowingTree():
    RANDOM = lambda self, cells: cells[random.randrange(len(cells))]
    NEWEST = lambda self, cells: cells[len(cells)-1]
    OLDEST = lambda self, cells: cells[0]

    def __init__(self, maze, weight, methods):
        self.maze = maze
        self.weight = weight
        self.cells = []
        self.methods = methods

    def generate(self):
        self.cells.append(self.maze.get_random_cell())
        while self.cells:
            cell = self.pick_cell()
            neighbor, direction = cell.get_random_closed_neighbor(self.weight)
            if not neighbor:
                self.cells.remove(cell)
                continue
            cell.connect_to_cell(direction)
            self.cells.append(neighbor)

    def pick_cell(self):
        value = random.random()
        for method, chance in self.methods:
            value -= chance
            if value <= 0:
                return method(self, self.cells)
        return self.methods[len(self.methods)-1][0](self, self.cells)