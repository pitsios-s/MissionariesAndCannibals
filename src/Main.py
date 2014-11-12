#!/usr/bin/python3

from Solver import Solver
from World import World

if __name__ == "__main__":
    world = World(3, 3)
    solver = Solver(world)

    solution = solver.find_solution()
    if not solution == None:
        print("SOLUTION FOUND!\n")
        solution.print_history()
    else:
        print("NO SOLUTION FOUND.")
