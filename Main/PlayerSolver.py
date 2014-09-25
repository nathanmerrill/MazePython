from Directions import Directions
import pygame


class PlayerSolver:

    def __init__(self, maze):
        self.maze = maze
        self.start = (0, 0)
        self.moves = 0
        self.finish = (maze.width-1, maze.height-1)
        self.player = self.maze.get(self.start)

    def solve(self):
        while True:
            self.player.active = True
            self.maze.draw()
            if self.player.coordinates == self.finish:
                return self.moves
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.KEYDOWN:
                    self.move_player(event.key)

    def move_player(self, key):
        direction = None
        key_to_direction = {
            pygame.K_s: Directions.BOTTOM,
            pygame.K_w: Directions.TOP,
            pygame.K_d: Directions.RIGHT,
            pygame.K_a: Directions.LEFT}
        if key not in key_to_direction:
            return
        direction = key_to_direction[key]
        next_spot = self.player.get_neighbor(Directions(direction))
        if not next_spot:
            return
        self.player = next_spot
        self.player.active = False
        self.moves+=1


