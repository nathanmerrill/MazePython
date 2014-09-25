import pygame
import random
import Utils
import colorsys
import sys
from Directions import Directions
from time import sleep


class MazeGraphics:
    def __init__(self, grid_increment, seconds_to_generate):
        self.grid_increment = grid_increment
        pygame.init()
        self.dimensions = None
        self.screen = None
        self.maze = None
        self.seconds_to_generate = seconds_to_generate
        self.delay = None
        bg_color_hls = (random.random(), random.random(), random.random()/2+.25)
        fg_color_hls = ((bg_color_hls[0]+.5) % 1.0, (bg_color_hls[1] + .5) % 1.0, bg_color_hls[2])
        active_color_hls = (((bg_color_hls[0]+fg_color_hls[0])/2.0),
                            ((bg_color_hls[1]+fg_color_hls[1])/2.0), bg_color_hls[2])
        self.bg_color = Utils.multiply_tuple(colorsys.hls_to_rgb(*bg_color_hls), 256)
        self.fg_color = Utils.multiply_tuple(colorsys.hls_to_rgb(*fg_color_hls), 256)
        self.active_color = Utils.multiply_tuple(colorsys.hls_to_rgb(*active_color_hls), 256)
        self.wall_width = 1 if self.grid_increment < 5 else 2

    def init(self, maze):
        self.dimensions = Utils.multiply_tuple(maze.dimensions, self.grid_increment)
        self.screen = pygame.display.set_mode(self.dimensions, 0, 32)
        self.delay = self.seconds_to_generate/(2.0 * maze.width * maze.height)
        pygame.display.set_caption("Maze")
        pygame.display.flip()

    def __del__(self):
        pygame.display.quit()

    def draw_maze(self, maze):
        for line in maze.grid:
            for cell in line:
                self.draw_cell(cell)
        self.update()

    def update(self):
        self.screen.blit(self.screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def draw_cells(self, cells):
        for cell in cells:
            self.draw_cell(cell)
        sleep(self.delay)
        self.update()

    def draw_cell(self, cell):
        cell_color = self.active_color if cell.active else None
        if not cell_color:
            cell_color = self.bg_color if cell.open else self.fg_color
        cell_coordinates = Utils.multiply_tuple(cell.coordinates, self.grid_increment)
        rect = pygame.Rect(cell_coordinates, (self.grid_increment, self.grid_increment))
        self.screen.fill(cell_color, rect)
        if cell.open:
            for direction in Directions.get_all():
                if not cell.has_wall(direction):
                    continue
                coordinates = Directions.to_coordinates(direction)
                coordinates = list(coordinates + Utils.add_tuples(coordinates, (1, 1)))
                for x in xrange(len(coordinates)):
                    if coordinates[x] < 0:
                        coordinates[x] = 0
                    elif coordinates[x] > 1:
                        coordinates[x] = 1
                    coordinates[x] = coordinates[x] * self.grid_increment
                pygame.draw.line(self.screen, self.fg_color, Utils.add_tuples(cell_coordinates, tuple(coordinates[:2])),
                                 Utils.add_tuples(cell_coordinates, tuple(coordinates[2:])), self.wall_width)