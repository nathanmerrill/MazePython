from Main.MazeTypes.KruskalsMaze import KruskalsMaze
from Main.MazeTypes.EllersMaze import EllersMaze
from Main.MazeTypes.DividingMaze import DividingMaze
from Main.MazeTypes.HuntAndKill import HuntAndKill
from Main.MazeTypes.GrowingTree import GrowingTree
from Main.Maze import Maze
from Main.Graphics import MazeGraphics
from Main.Solver import Solver
from Main.PlayerSolver import PlayerSolver
from Main.Braider import Braider
import pygame


def input_to_method(i):
    if i == 1:
        return GrowingTree.NEWEST
    elif i == 2:
        return GrowingTree.RANDOM
    elif i == 3:
        return GrowingTree.OLDEST


def input_to_maze_type(i):
    if i == 1:
        return KruskalsMaze
    elif i == 2:
        return GrowingTree
    elif i == 3:
        return HuntAndKill
    elif i == 4:
        return DividingMaze
    else:
        return EllersMaze


def input_to_solver(i):
    if i == 1:
        return PlayerSolver
    else:
        return Solver


maze_type = int(raw_input("What kind of maze do you want:\n1. "
                          "Kruskal's,\n2. Growing Tree\n3. Hunt and Kill\n"
                          "4. Dividing\n5. Eller's\n"))
selection = []
if maze_type == 2:
    how_to_select = int(raw_input("How should I select the squares?\n1. Newest\n2. Random"
                                  "\n3. Oldest\n4. Multiple ways\n"))
    if how_to_select == 4:
        percentage = 0
        while percentage < 100:
            method = int(raw_input("What method?\n1. Newest\n2. Random\n3. Oldest\n"))
            chance = int(raw_input("How often should I use that method (in percentage):"))
            percentage += chance
            selection.append((input_to_method(method), chance/100.0))
    else:
        selection.append((input_to_method(how_to_select), 1))
weight = int(raw_input("How do you want it weighted towards Up/Down(0) or Left/Right(100)?:"))
maze_height = int(raw_input("How tall do you want the maze:"))
maze_width = int(raw_input("How wide do you want the maze:"))
loading_duration = int(raw_input("How many seconds do you want the generation to take (inaccurate at large maze):"))
square_size = int(raw_input("How many pixels wide do you want the squares:"))
solve_maze = int(raw_input("Do you (1) want to solve the maze, or should I (2):"))

graphics = MazeGraphics(square_size, loading_duration)
maze = Maze(maze_width, maze_height, graphics)

generator_class = input_to_maze_type(maze_type)
if generator_class == GrowingTree:
    generator = generator_class(maze, weight/100.0, selection)
else:
    generator = generator_class(maze, weight/100.0)
generator.generate()

Braider(maze, 30).braid()

solver = input_to_solver(solve_maze)
steps = solver(maze).solve()
if steps > 0:
    print "Solved in "+str(steps)+" steps."
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True