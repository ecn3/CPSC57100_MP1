""" 
Christian Nelson
9/11/2020
CPSC-57100-002, Fall 2020
Machine Problem 1: Sliding Puzzle
"""

# Imports
import numpy as np
import queue

# Formats
move_fmt = "MOVE {} ACTION: {}"

class PuzzleState():
    SOLVED_PUZZLE = np.arange(9).reshape((3, 3))

    def __init__(self,conf,g,predState):
        self.puzzle = conf
        self.gcost = g
        self._compute_heuristic_cost()
        #self.fcost = self.gcost + self.hcost
        self.pred = predState
        self.zeroloc = np.argwhere(self.puzzle == 0)[0]
        self.action_from_pred = None
    
    def __hash__(self):
        return tuple(self.puzzle.ravel()).__hash__() 
    
    def _compute_heuristic_cost(self):
        """ Updates the heuristic function value for use in A* """

    
    def is_goal(self):
        return np.array_equal(PuzzleState.SOLVED_PUZZLE,self.puzzle)
    
    def __eq__(self, other):
        return np.array_equal(self.puzzle, other.puzzle)
    
    def __lt__(self, other):
        return self.fcost < other.fcost
    
    def __str__(self):
        return np.str(self.puzzle)

    move = 0
    
    def show_path(self): 
        if self.pred is not None:
            self.pred.show_path()
        
        if PuzzleState.move==0:
            print('START')
        else:
            print('Move',PuzzleState.move, 'ACTION:', self.action_from_pred)
        PuzzleState.move = PuzzleState.move + 1
        print(self)
    
    def can_move(self, direction):
        zero_position = np.argwhere(self.puzzle == 0)[0]
        # Test if 0 tile can move up
        if zero_position[0] > 0:
            print(zero_position, "up")
        # Test if 0 tile can move down    
        if zero_position[0] < 2:
            print(zero_position, "down")
        # Test if 0 tile can move up
        if zero_position[1] > 0:
            print(zero_position, "left")
        # Test if 0 tile can move down    
        if zero_position[1] < 2:
            print(zero_position, "right")
        
    def gen_next_state(self, direction):
        """ TODO """

            

print('Artificial Intelligence')
print('MP1: A* for Sliding Puzzle')
print('SEMESTER: Fall 2020')
print('NAME: Christian Nelson')
print("")


frontier = queue.PriorityQueue()
a = np.loadtxt('mp1input.txt', dtype=np.int32)
start_state = PuzzleState(a,0,None)

frontier.put(start_state)

closed_set = set()

num_states = 0
while not frontier.empty():
    next_state = frontier.get() 
    num_states = num_states + 1

    if next_state.is_goal():
        next_state.show_path()
        break
    
    closed_set.add(next_state)
    
    possible_moves = ['up','down','left','right']
    for move in possible_moves:
        if next_state.can_move(move):
            neighbor = next_state.gen_next_state(move)
            if neighbor in closed_set:
                continue 
            if neighbor not in frontier.queue:                           
                frontier.put(neighbor)

print('\nNumber of states visited =',num_states)

    