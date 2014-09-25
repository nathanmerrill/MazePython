import random
from ..Directions import Directions


class EllersMaze():
    def __init__(self, maze, weight):
        self.maze = maze
        self.weight = weight

    def generate(self):
        states = range(self.maze.width)
        for y in xrange(self.maze.height):
            states = self.generate_line(y, states)

    def generate_line(self, y, states):
        self.connect_neighbors(y, states)
        if y == self.maze.height-1:
            while not all(x == states[0] for x in states):
                self.connect_neighbors(y, states)
        else:
            states = self.connect_lines(y, states)
        return states

    def connect_neighbors(self, y, states):
        for x in xrange(self.maze.width-1):
            if states[x] != states[x+1]:
                if random.random() < self.weight:
                    self.maze.get((x, y)).connect_to_cell(Directions(Directions.RIGHT))
                    to_replace = states[x+1]
                    for index, value in enumerate(states):
                        if value == to_replace:
                            states[index] = states[x]

    def connect_lines(self, y, states):
        new_states = range(max(states)+1, max(states)+1+len(states))
        states_left = {state for state in states}
        states_to_pick = range(len(states))
        random.shuffle(states_to_pick)
        for index in states_to_pick:
            if states[index] in states_left or random.random() >= self.weight:
                self.maze.get((index, y)).connect_to_cell(Directions(Directions.BOTTOM))
                new_states[index] = states[index]
                if states[index] in states_left:
                    states_left.remove(states[index])
        return new_states
