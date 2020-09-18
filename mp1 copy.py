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
        self.hcost = self._compute_heuristic_cost()
        self.fcost = self.gcost + self.hcost
        self.pred = predState
        self.zeroloc = np.argwhere(self.puzzle == 0)[0]
        self.action_from_pred = None
    
    def __hash__(self):
        return tuple(self.puzzle.ravel()).__hash__() 
    
    def _compute_heuristic_cost(self): # DONE
        # Current Locations
        loc_of_1_current = np.argwhere(self.puzzle == 1)[0]
        loc_of_2_current = np.argwhere(self.puzzle == 2)[0]
        loc_of_3_current = np.argwhere(self.puzzle == 3)[0]
        loc_of_4_current = np.argwhere(self.puzzle == 4)[0]
        loc_of_5_current = np.argwhere(self.puzzle == 5)[0]
        loc_of_6_current = np.argwhere(self.puzzle == 6)[0]
        loc_of_7_current = np.argwhere(self.puzzle == 7)[0]
        loc_of_8_current = np.argwhere(self.puzzle == 8)[0]

        # Goal Locations
        loc_of_1_goal = np.argwhere(PuzzleState.SOLVED_PUZZLE == 1)[0]
        loc_of_2_goal = np.argwhere(PuzzleState.SOLVED_PUZZLE == 2)[0]
        loc_of_3_goal = np.argwhere(PuzzleState.SOLVED_PUZZLE == 3)[0]
        loc_of_4_goal = np.argwhere(PuzzleState.SOLVED_PUZZLE == 4)[0]
        loc_of_5_goal = np.argwhere(PuzzleState.SOLVED_PUZZLE == 5)[0]
        loc_of_6_goal = np.argwhere(PuzzleState.SOLVED_PUZZLE == 6)[0]
        loc_of_7_goal = np.argwhere(PuzzleState.SOLVED_PUZZLE == 7)[0]
        loc_of_8_goal = np.argwhere(PuzzleState.SOLVED_PUZZLE == 8)[0]

        # Compute Manhattan distance
        manhattan_distance_1 = abs(loc_of_1_current[0] - loc_of_1_goal[0]) + abs(loc_of_1_current[1] - loc_of_1_goal[1])
        manhattan_distance_2 = abs(loc_of_2_current[0] - loc_of_2_goal[0]) + abs(loc_of_2_current[1] - loc_of_2_goal[1])
        manhattan_distance_3 = abs(loc_of_3_current[0] - loc_of_3_goal[0]) + abs(loc_of_3_current[1] - loc_of_3_goal[1])
        manhattan_distance_4 = abs(loc_of_4_current[0] - loc_of_4_goal[0]) + abs(loc_of_4_current[1] - loc_of_4_goal[1])
        manhattan_distance_5 = abs(loc_of_5_current[0] - loc_of_5_goal[0]) + abs(loc_of_5_current[1] - loc_of_5_goal[1])
        manhattan_distance_6 = abs(loc_of_6_current[0] - loc_of_6_goal[0]) + abs(loc_of_6_current[1] - loc_of_6_goal[1])
        manhattan_distance_7 = abs(loc_of_7_current[0] - loc_of_7_goal[0]) + abs(loc_of_7_current[1] - loc_of_7_goal[1])
        manhattan_distance_8 = abs(loc_of_8_current[0] - loc_of_8_goal[0]) + abs(loc_of_8_current[1] - loc_of_8_goal[1])

        total_manhattan_distance = manhattan_distance_1+manhattan_distance_2+manhattan_distance_3+manhattan_distance_4+manhattan_distance_5+manhattan_distance_6+manhattan_distance_7+manhattan_distance_8
        #print("Manhattan Distance: ",total_manhattan_distance)
        return total_manhattan_distance

    
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
    
    def can_move(self, direction): # DONE
        # Get zero location
        zero_position = np.argwhere(self.puzzle == 0)[0]

        # Test if 0 tile can move up
        if direction == "up" and zero_position[0] > 0:
            return True
        # Test if 0 tile can move down   
        if direction == "down" and zero_position[0] < 2:
            return True
        # Test if 0 tile can move up
        if direction == "left" and zero_position[1] > 0:
            return True
        # Test if 0 tile can move down       
        if direction == "right" and zero_position[1] < 2:
            return True

    def gen_next_state(self, direction):
        # Get zero location
        zero_position = np.argwhere(self.puzzle == 0)[0]

        # Create Next state
        next_state = PuzzleState(self.puzzle, (self.gcost+1),self.pred)

        # Make move
        if direction == "up":
            self.puzzle[zero_position[0],zero_position[1]] = self.puzzle[zero_position[0]-1,zero_position[1]]
            self.puzzle[zero_position[0]-1,zero_position[1]] = 0

        if direction == "down":
            self.puzzle[zero_position[0],zero_position[1]] = self.puzzle[zero_position[0]+1,zero_position[1]]
            self.puzzle[zero_position[0]+1,zero_position[1]] = 0

        if direction == "right":
            self.puzzle[zero_position[0],zero_position[1]] = self.puzzle[zero_position[0],zero_position[1]+1]
            self.puzzle[zero_position[0],zero_position[1]+1] = 0

        if direction == "left":
            self.puzzle[zero_position[0],zero_position[1]] = self.puzzle[zero_position[0],zero_position[1]-1]
            self.puzzle[zero_position[0],zero_position[1]-1] = 0
        
        # Make move
        next_state.puzzle = self.puzzle

        # update zeroloc
        next_state.zeroloc = np.argwhere(next_state.puzzle == 0)[0]

        # update hcost
        next_state.hcost = next_state._compute_heuristic_cost()

        # update fcost
        next_state.fcost = next_state.gcost + next_state.hcost

        # Update action from pred
        next_state.action_from_pred = direction



print('Artificial Intelligence')
print('MP1: A* for Sliding Puzzle')
print('SEMESTER: Fall 2020')
print('NAME: Christian Nelson')
print("")


# load random start state onto frontier priority queue
frontier = queue.PriorityQueue()
a = np.loadtxt('mp1input.txt', dtype=np.int32)
start_state = PuzzleState(a,0,None)

frontier.put(start_state)

closed_set = set()

num_states = 0
while not frontier.empty():
    #  choose state at front of priority queue
    next_state = frontier.get()
    num_states = num_states + 1

    #  if goal then quit and return path
    if next_state.is_goal():
        next_state.show_path()
        break
    
    # Add state chosen for expansion to closed_set
    closed_set.add(next_state)
    
    # Expand state (up to 4 moves possible)
    possible_moves = ['up','down','left','right']
    for move in possible_moves:
        if next_state.can_move(move):
            neighbor = next_state.gen_next_state(move)
            if neighbor in closed_set:
                continue
            if neighbor not in frontier.queue:                           
                frontier.put(neighbor)
            # If it's already in the frontier, it's gauranteed to have lower cost, so no need to update

print('\nNumber of states visited =',num_states)