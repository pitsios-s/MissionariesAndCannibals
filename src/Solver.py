#!/usr/bin/python3

class Solver:
    """Every instance of this class, will be used to solve the sheep-and-wolves
        problem, with the help of search algorithms, such as BFS and DFS."""

    def __init__(self, world):
           self.world = world

    def find_solution(self):
        """Finds a solution for the world given, if any and returns it."""
        return self.__find_solution_bfs()

    def __find_solution_bfs(self):
        """Searches for solutions, using the BFS algorithm."""

        # The worlds that remain to be explored.
        worlds_to_explore = [self.world]

        # Keep a set of worlds allready created, in order to avoid duplicates.
        worlds_visited = []

        # Now search for possible solutions.
        while len(worlds_to_explore) > 0:
            world = worlds_to_explore.pop(0)

            if world not in worlds_visited:
                worlds_visited.append(world)
                if world.win():
                    return world
                else:
                    neighboor_worlds = world.get_neighboors()
                    for neighboor in neighboor_worlds:
                        worlds_to_explore.append(neighboor)
