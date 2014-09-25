import random
from Cell import Cell


class Maze:
    def __init__(self, width, height, graphics):
        self.grid = []
        for i in xrange(width):
            inner = []
            for j in xrange(height):
                inner.append(Cell(i, j, self))
            self.grid.append(inner)
        self.dimensions = width, height
        self.width = width
        self.height = height
        self.graphics = graphics
        graphics.init(self)

    def draw(self, cells=None):
        if not cells:
            self.graphics.draw_maze(self)
        else:
            self.graphics.draw_cells(cells)

    def __str__(self):
        string = ""
        for line in self.grid:
            for cell in line:
                string += str(cell)
            string += "\n"
        return string

    def get(self, coordinates):
        if coordinates[0] < 0 or coordinates[1] < 0 \
                or coordinates[1] >= self.height or coordinates[0] >= self.width:
            return None
        return self.grid[coordinates[0]][coordinates[1]]

    def get_random_cell(self):
        return self.get((random.randrange(self.width), random.randrange(self.height)))
