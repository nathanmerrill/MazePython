from Cell import Directions
import Utils
import random

class Braider:
    def __init__(self, maze, percent_braided):
        self.maze = maze
        self.percent = percent_braided

    def braid(self):
        dead_ends = []
        for line in self.maze.grid:
            for cell in line:
                if len(cell.get_connected_neighbors()) == 1:
                    dead_ends.append(cell)
        for cell in dead_ends:
            if cell.get_connected_neighbors() != 1 and random.random() > self.percent:
                continue
            d = None
            n = None
            for direction in Directions.get_all_random(.5):
                n = self.get_neighbor_wrap(cell, direction)
                if not d or n.get_connected_neighbors() == 1:
                    d = direction
            cell.walls[d] = False
            n.walls[d.get_opposite()] = False
            cell.grid.draw([cell, n])

    def get_neighbor_wrap(self, cell, direction):
        neighbor = list(Utils.add_tuples(cell.coordinates, direction.to_coordinates()))
        if neighbor[0] < 0:
            neighbor[0] += self.maze.width
        elif neighbor[0] >= self.maze.width:
            neighbor[0] -= self.maze.width
        if neighbor[1] < 0:
            neighbor[1] += self.maze.height
        elif neighbor[1] >= self.maze.height:
            neighbor[1] -= self.maze.height
        return self.maze.get(tuple(neighbor))









