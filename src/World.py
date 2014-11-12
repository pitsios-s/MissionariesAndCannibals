#!/usr/bin/python3

from State import State

class World:
    """Every instance of this class represents the world of the game,
        in a specific state."""

    def __init__(self, missionaries = 3, cannibals = 3,
                 state = None, history = None):
        self.missionaries = missionaries
        self.cannibals = cannibals

        # The current state of the world.
        if state:
            self.state = state
        else:
            self.state = State(self.missionaries, self.cannibals,
                                self.missionaries, 0, self.cannibals, 0)

        #A list of states that resulted in the current state.
        if history:
            self.history = history
        else:
            self.history = []

    def __eq__(self, other):
        if not isinstance(other, World):
            return False

        return self.state.__eq__(other.state)

    def win(self):
        """Returns true if we have accomplished the goal, which is to move every
            missionary and cannibal to the right side."""
        return self.state.is_final()

    def print_history(self):
        """Prints the history of moves that resulted in the current snapshot
            of the world."""
        for state in self.history:
            print(str(state.get_description()))
        print(str(self.state.get_description()) + "\n")

    def get_neighboors(self):
        """Returns all the valid World objects, that can derive from the
            current world."""
        neighboor_states = self.state.get_neighboors()
        neighboor_worlds = []

        for neighboor in neighboor_states:
            new_history = list(self.history)
            new_history.append(self.state.copy())
            neighboor_worlds.append(World(self.missionaries, self.cannibals,
            neighboor.copy(), new_history))

        return neighboor_worlds
