import Utils


class Solver:
    def __init__(self, maze):
        self.maze = maze
        self.goal = (self.maze.width-1, self.maze.height-1)
        self.visited = {}
        self.start = maze.get((0, 0))

    def solve(self):
        paths = [Path(self.start)]
        cells_visited = {self.start}
        while paths:
            next_paths = []
            for path in paths:
                if path.cell.coordinates == self.goal:
                    path_array = path.build_list()
                    for cell in path_array:
                        cell.active = True
                    self.maze.draw()
                    return len(path_array)
                for neighbor, direction in path.cell.get_connected_neighbors():
                    if neighbor in cells_visited:
                        continue
                    next_paths.append(Path(neighbor, path))
                    cells_visited.add(neighbor)

            paths = next_paths
        return -1


class Path:
    def __init__(self, cell, last=None):
        self.cell = cell
        self.last = last

    def build_list(self):
        path = [self.cell]
        last = self.last
        while last:
            path.insert(0,last.cell)
            last = last.last
        return path



