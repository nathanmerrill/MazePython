from ..Maze import *
import random
from ..Directions import Directions


class DividingMaze():
    def __init__(self, maze, weight):
        self.maze = maze
        self.weight = weight
        for line in maze.grid:
            for cell in line:
                for key in cell.walls:
                    cell.walls[key] = False
                cell.open = True
                if cell.coordinates[0] == 0:
                    cell.walls[Directions(Directions.LEFT)] = True
                elif cell.coordinates[0] == maze.width-1:
                    cell.walls[Directions(Directions.RIGHT)] = True
                if cell.coordinates[1] == 0:
                    cell.walls[Directions(Directions.TOP)] = True
                elif cell.coordinates[1] == maze.height-1:
                    cell.walls[Directions(Directions.BOTTOM)] = True

    def generate(self):
        self.maze.draw()
        rectangles = [((0, 0), (self.maze.width, self.maze.height))]
        while rectangles:
            random.shuffle(rectangles)
            next_rectangles = []
            for tl, br in rectangles:
                new_tl, new_br = self.split_rectangles(tl, br)
                if not new_tl:
                    continue
                next_rectangles.append((tl, new_br))
                next_rectangles.append((new_tl, br))
            rectangles = next_rectangles

    def split_rectangles(self, tl, br):
        #for x in range(2):
        #    if br[x] - tl[x] < br[1-x] - tl[1-x]:
        #        return self.split(tl, br, x)
        width = br[0] - tl[0]
        height = br[1] - tl[1]
        draw_vertical = width*1.0/(width+height) + random.random()-.5 > self.weight
        return self.split(tl, br, 1 if draw_vertical else 0)

    def split(self, tl, br, index):
        if br[1-index] - tl[1-index] < 2:
            return None, None
        length = br[1-index] - tl[1-index]
        a = tl[1-index]+random.randrange(length-1)
        walls = range(tl[index], br[index])
        walls.pop(random.randrange(len(walls)))
        for b in walls:
            self.maze.get((a, b)[::(index*2)-1]).disconnect_from_cell(Directions(Directions.BOTTOM+index))
        return (a+1, tl[index])[::(index*2)-1], (a+1, br[index])[::(index*2)-1]
