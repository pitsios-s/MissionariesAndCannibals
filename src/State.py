#!/usr/bin/python3

from enum import Enum

class BoatContent(Enum):
    missionary = "MISSIONARY"
    cannibal = "CANNIBAL"
    empty = "EMPTY"

class BoatPosition(Enum):
    left = "LEFT"
    right = "RIGHT"

class Move(Enum):
    init = "INITIAL STATE"
    mv_left = "MOVE LEFT"
    mv_right = "MOVE RIGHT"
    pick_missionary = "PICK MISSIONARY"
    pick_cannibal = "PICK CANNIBAL"
    leave_missionary = "LEAVE MISSIONARY"
    leave_cannibal = "LEAVE CANNIBAL"

class State:
    """Every instance of this class represents a state of the world."""

    def __init__(self, total_missionaries = 3, total_cannibals = 3,
                missionaries_left = 3, missionaries_right = 0,
                cannibals_left = 3, cannibals_right = 0,
                boat_pos = BoatPosition.left,
                first_passenger = BoatContent.empty,
                second_passenger = BoatContent.empty, description = Move.init):

        #The total number of missionaries and cannibals.
        self.total_missionaries = total_missionaries
        self.total_cannibals = total_cannibals

        #The number of missionaries that are on the left side of the lake.
        self.missionaries_left = missionaries_left

        #The number of missionaries that are on the right side of the lake.
        self.missionaries_right = missionaries_right

        #The number of cannibals that are on the left side of the lake.
        self.cannibals_left = cannibals_left

        #The number of cannibals that are on the right side of the lake.
        self.cannibals_right = cannibals_right

        #The position of the boat.
        self.boat_pos = boat_pos

        #The contents of the boat.
        self.first_passenger = first_passenger
        self.second_passenger = second_passenger

        #A description of the previous move, that resulted in the current state.
        self.description = description

    def __eq__(self, other):
        if not isinstance(other, State):
            return false

        return self.total_missionaries == other.total_missionaries and \
               self.total_cannibals == other.total_cannibals       and \
               self.missionaries_left == other.missionaries_left   and \
               self.missionaries_right == other.missionaries_right and \
               self.cannibals_left == other.cannibals_left         and \
               self.cannibals_right == other.cannibals_right       and \
               self.boat_pos == other.boat_pos                     and \
               self.first_passenger == other.first_passenger       and \
               self.second_passenger == other.second_passenger     and \
               self.description == other.description
    
    def __str__(self):
        return  "Missionaries left: "         + str(self.missionaries_left)  + \
                "\nCannibals left: "          + str(self.cannibals_left)     + \
                "\nMissionaries right: "      + str(self.missionaries_right) + \
                "\nCannibals right: "         + str(self.cannibals_right)    + \
                "\nBoat position: "           + self.boat_pos.value          + \
                "\nBoat's First Passenger: "  + self.first_passenger.value   + \
                "\nBoat's Second Passenger: " + self.second_passenger.value  + \
                "\nDescription: "             + self.description.value       + "\n"

    def get_neighboors(self):
        """This method returns a list of all the valid states that can derive
            from the current one."""
        neighboors = []

        if self.__can_move_left():
            neighboors.append(State(self.total_missionaries,
                                    self.total_cannibals,
                                    self.missionaries_left,
                                    self.missionaries_right,
                                    self.cannibals_left, self.cannibals_right,
                                    BoatPosition.left, self.first_passenger,
                                    self.second_passenger, Move.mv_left))

        if self.__can_move_right():
            neighboors.append(State(self.total_missionaries,
                                    self.total_cannibals,
                                    self.missionaries_left,
                                    self.missionaries_right,
                                    self.cannibals_left, self.cannibals_right,
                                    BoatPosition.right, self.first_passenger,
                                    self.second_passenger, Move.mv_right))

        if self.__can_pick_missionary_from_left():

            if self.first_passenger == BoatContent.empty:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left - 1,
                                        self.missionaries_right,
                                        self.cannibals_left,
                                        self.cannibals_right, self.boat_pos,
                                        BoatContent.missionary,
                                        self.second_passenger,
                                        Move.pick_missionary))

            elif self.second_passenger == BoatContent.empty:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left - 1,
                                        self.missionaries_right,
                                        self.cannibals_left,
                                        self.cannibals_right, self.boat_pos,
                                        self.first_passenger,
                                        BoatContent.missionary,
                                        Move.pick_missionary))

        if self.__can_pick_missionary_from_right():

            if self.first_passenger == BoatContent.empty:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right - 1,
                                        self.cannibals_left,
                                        self.cannibals_right, self.boat_pos,
                                        BoatContent.missionary,
                                        self.second_passenger,
                                        Move.pick_missionary))

            elif self.second_passenger == BoatContent.empty:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right - 1,
                                        self.cannibals_left,
                                        self.cannibals_right, self.boat_pos,
                                        self.first_passenger,
                                        BoatContent.missionary,
                                        Move.pick_missionary))

        if self.__can_pick_cannibal_from_left():

            if self.first_passenger == BoatContent.empty:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right,
                                        self.cannibals_left - 1,
                                        self.cannibals_right, self.boat_pos,
                                        BoatContent.cannibal,
                                        self.second_passenger,
                                        Move.pick_cannibal))

            elif self.second_passenger == BoatContent.empty:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right,
                                        self.cannibals_left - 1,
                                        self.cannibals_right, self.boat_pos,
                                        self.first_passenger,
                                        BoatContent.cannibal,
                                        Move.pick_cannibal))

        if self.__can_pick_cannibal_from_right():

            if self.first_passenger == BoatContent.empty:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right,
                                        self.cannibals_left,
                                        self.cannibals_right - 1, self.boat_pos,
                                        BoatContent.cannibal,
                                        self.second_passenger,
                                        Move.pick_cannibal))

            elif self.second_passenger == BoatContent.empty:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right,
                                        self.cannibals_left,
                                        self.cannibals_right - 1, self.boat_pos,
                                        self.first_passenger,
                                        BoatContent.cannibal,
                                        Move.pick_cannibal))

        if self.__can_leave_missionary_to_left():

            if self.first_passenger == BoatContent.missionary:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left + 1,
                                        self.missionaries_right,
                                        self.cannibals_left,
                                        self.cannibals_right, self.boat_pos,
                                        BoatContent.empty,
                                        self.second_passenger,
                                        Move.leave_missionary))

            elif self.second_passenger == BoatContent.missionary:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left + 1,
                                        self.missionaries_right,
                                        self.cannibals_left,
                                        self.cannibals_right, self.boat_pos,
                                        self.first_passenger,
                                        BoatContent.empty,
                                        Move.leave_missionary))

        if self.__can_leave_missionary_to_right():

            if self.first_passenger == BoatContent.missionary:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right + 1,
                                        self.cannibals_left,
                                        self.cannibals_right, self.boat_pos,
                                        BoatContent.empty,
                                        self.second_passenger,
                                        Move.leave_missionary))

            elif self.second_passenger == BoatContent.missionary:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right + 1,
                                        self.cannibals_left,
                                        self.cannibals_right, self.boat_pos,
                                        self.first_passenger, BoatContent.empty,
                                        Move.leave_missionary))

        if self.__can_leave_cannibal_to_left():

            if self.first_passenger == BoatContent.cannibal:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right,
                                        self.cannibals_left + 1,
                                        self.cannibals_right, self.boat_pos,
                                        BoatContent.empty,
                                        self.second_passenger,
                                        Move.leave_cannibal))

            elif self.second_passenger == BoatContent.cannibal:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right,
                                        self.cannibals_left + 1,
                                        self.cannibals_right, self.boat_pos,
                                        self.first_passenger, BoatContent.empty,
                                        Move.leave_cannibal))


        if self.__can_leave_cannibal_to_right():

            if self.first_passenger == BoatContent.cannibal:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right,
                                        self.cannibals_left,
                                        self.cannibals_right + 1, self.boat_pos,
                                        BoatContent.empty,
                                        self.second_passenger,
                                        Move.leave_cannibal))

            elif self.second_passenger == BoatContent.cannibal:
                neighboors.append(State(self.total_missionaries,
                                        self.total_cannibals,
                                        self.missionaries_left,
                                        self.missionaries_right,
                                        self.cannibals_left,
                                        self.cannibals_right + 1, self.boat_pos,
                                        self.first_passenger,
                                        BoatContent.empty, Move.leave_cannibal))

        return neighboors

    def get_missionaries_left(self):
        """Returns the number of missionaries, that are at the left side of the
            lake."""
        return self.missionaries_left

    def get_missionaries_right(self):
        """Returns the number of missionaries, that are at the right side of the
            lake."""
        return self.missionaries_right

    def get_cannibals_left(self):
        """Returns the number of cannibals, that are at the left side of the
            lake."""
        return self.cannibals_left

    def get_cannibals_right(self):
        """Returns the number of cannibals, that are at the right side of the
            lake."""
        return self.cannibals_right

    def get_description(self):
        """Returns the description of the previous move, that resulted in the
        current state."""
        return self.description.value

    def copy(self):
        """Returns a copy of the current state."""
        return State(self.total_missionaries, self.total_cannibals,
                     self.missionaries_left, self.missionaries_right,
                     self.cannibals_left, self.cannibals_right, self.boat_pos,
                     self.first_passenger, self.second_passenger,
                     self.description)

    def is_final(self):
        """Returns true, if the current state is a final state,
            false otherwise."""
        return self.total_missionaries == self.missionaries_right and \
                self.total_cannibals == self.cannibals_right      and \
                self.boat_pos == BoatPosition.right

    ### Helper functions to determine which valid states can be created ###
    ### from the current one. ###

    def __has_first_passenger(self):
        """Returns whether or not, the first seat of the boat is empty."""
        return not self.first_passenger == BoatContent.empty

    def __has_second_passenger(self):
        """Returns whether or not, the second seat of the boat is empty."""
        return not self.second_passenger == BoatContent.empty

    def __boat_empty(self):
        """Returns true if the boat is empty, false otherwise."""
        return not self.__has_first_passenger() and \
                not self.__has_second_passenger()

    def __boat_full(self):
        """Returns true if both of the boats available seats are  reserved."""
        return self.__has_first_passenger() and self.__has_second_passenger()

    def __missionaries_on_boat(self):
        """Returns the number of missionaries inside the boat."""
        total = 0

        if self.first_passenger == BoatContent.missionary:
            total += 1

        if self.second_passenger == BoatContent.missionary:
            total += 1

        return total

    def __cannibals_on_boat(self):
        """Returns the number of cannibals inside the boat."""
        total = 0

        if self.first_passenger == BoatContent.cannibal:
            total += 1

        if self.second_passenger == BoatContent.cannibal:
            total += 1

        return total

    def __can_move_left(self):
        """Returns true if the boat can move to the left side of the lake,
            false otherwise."""
        if (not self.__boat_empty()) and (self.boat_pos == BoatPosition.right):
            missionaries_on_boat = self.__missionaries_on_boat()
            cannibals_on_boat = self.__cannibals_on_boat()

            return ( (self.missionaries_left + missionaries_on_boat >=
                        self.cannibals_left + cannibals_on_boat) or \
                        (self.missionaries_left + missionaries_on_boat == 0) ) and \
                    ( (self.missionaries_right >= self.cannibals_right) or \
                        (self.missionaries_right == 0) )
        else:
            return False

    def __can_move_right(self):
        """Returns true if the boat can move to the right side of the lake,
            false otherwise."""
        if (not self.__boat_empty()) and (self.boat_pos == BoatPosition.left):
            missionaries_on_boat = self.__missionaries_on_boat()
            cannibals_on_boat = self.__cannibals_on_boat()

            return ( (self.missionaries_right + missionaries_on_boat >=
                        self.cannibals_right + cannibals_on_boat) or \
                        (self.missionaries_right + missionaries_on_boat == 0) ) and \
                    ( (self.missionaries_left >= self.cannibals_left) or \
                        (self.missionaries_left == 0) )
        else:
            return False

    def __can_pick_missionary_from_left(self):
        """Returns true if we can pick a missionary from the left side of the
            lake, false otherwise."""
        return self.boat_pos == BoatPosition.left and \
                self.missionaries_left > 0 and \
                not self.__boat_full()

    def __can_pick_missionary_from_right(self):
        """Returns true if we can pick a missionary from the right side of the
            lake, false otherwise."""
        return self.boat_pos == BoatPosition.right and \
                self.missionaries_right > 0 and \
                not self.__boat_full()

    def __can_pick_cannibal_from_left(self):
        """Returns true if we can pick a cannibal from the left side of the
            lake, false otherwise."""
        return self.boat_pos == BoatPosition.left and \
                self.cannibals_left > 0 and \
                not self.__boat_full()

    def __can_pick_cannibal_from_right(self):
        """Returns true if we can pick a cannibal from the right side of the
            lake, false otherwise."""
        return self.boat_pos == BoatPosition.right and \
                self.cannibals_right > 0 and \
                not self.__boat_full()

    def __can_leave_missionary_to_left(self):
        """Returns true if we can leave a missionary to the left side of the
            lake, false otherwise."""
        return self.boat_pos == BoatPosition.left and \
                self.__missionaries_on_boat() > 0

    def __can_leave_missionary_to_right(self):
        """Returns true if we can leave a missionary to the right side of the
            lake, false otherwise."""
        return self.boat_pos == BoatPosition.right and \
                self.__missionaries_on_boat() > 0

    def __can_leave_cannibal_to_left(self):
        """Returns true if we can leave a cannibal to the left side of the lake,
            false otherwise."""
        return self.boat_pos == BoatPosition.left and \
                self.__cannibals_on_boat() > 0

    def __can_leave_cannibal_to_right(self):
        """Returns true if we can leave a cannibal to the right side of the
            lake, false otherwise."""
        return self.boat_pos == BoatPosition.right and \
                self.__cannibals_on_boat() > 0
