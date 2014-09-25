class KruskalsMaze():
    def __init__(self, maze, weight):
        self.maze = maze
        self.states = [x for x in xrange(maze.width*maze.height)]
        self.weight = weight
        self.sum = 0
        self.total = 0

    def generate(self):
        for _ in xrange(len(self.states)-1):
            while True:
                cell = self.maze.get_random_cell()
                if self.connect(cell):
                    break

    def connect(self, cell):
        state = self.get_state(cell)
        for neighbor in cell.get_random_neighbors(self.weight):
            if neighbor[1].is_vertical():
                self.sum += 1
            self.total += 1
            neighbor_state = self.get_state(neighbor[0])
            if neighbor_state == state:
                continue
            cell.connect_to_cell(neighbor[1])
            self.states[neighbor_state] = self.states[state]
            return True
        return False

    def get_state(self, cell):
        return self.update_state(self.cell_to_position(cell))

    def cell_to_position(self, cell):
        return cell.coordinates[0]+cell.coordinates[1]*self.maze.width

    def update_state(self, state):
        if self.states[state] == state:
            return state
        self.states[state] = self.update_state(self.states[state])
        return self.states[state]
