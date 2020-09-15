""" 
Christian Nelson
9/11/2020
CPSC-57100-002, Fall 2020
Machine Problem 1: Sliding Puzzle
"""

# Imports
import numpy as np
import queue

# PuzzleState class
class PuzzleState():
    SOLVED_PUZZLE = np.arange(9).reshape((3, 3))

    def __init__(self,conf,g,predState):
        self.puzzle = conf     # Configuration of the state
        self.gcost = g         # Path cost
        self.hcost()
        self._compute_heuristic_cost()  # Set heuristic cost
        self.fcost = self.gcost + self.hcost
        self.pred = predState  # Predecesor state
        self.zeroloc = np.argwhere(self.puzzle == 0)[0]
        self.action_from_pred = None

# load in start state into frontier priority queue
frontier = queue.PriorityQueue()
puzzle_input = np.loadtxt('mp1input.txt', dtype=np.int32)
start_state = PuzzleState(puzzle_input,0,None)



# Output
print('Artificial Intelligence')
print('MP1: A* for Sliding Puzzle')
print('SEMESTER: Fall 2020')
print('NAME: Christian Nelson')
print("")

