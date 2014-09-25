class HuntAndKill():
    def __init__(self, maze, weight):
        self.maze = maze
        self.states = [x for x in xrange(maze.width*maze.height)]
        self.weight = weight

    def generate(self):
        next_cell = self.maze.get_random_cell()
        while next_cell:
            self.walk(next_cell)
            next_cell = self.find_next_cell()

    def walk(self, step):
        while True:
            neighbor, direction = step.get_random_closed_neighbor(self.weight)
            if not neighbor:
                return
            step.connect_to_cell(direction)
            step = neighbor

    def find_next_cell(self):
        for line in self.maze.grid:
            for cell in line:
                if not cell.open:
                    neighbor, direction = cell.get_random_open_neighbor(self.weight)
                    if not neighbor:
                        continue
                    else:
                        cell.connect_to_cell(direction)
                        return cell
        return None


