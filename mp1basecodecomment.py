import numpy as np
import queue

class PuzzleState():
    # Defines goal state
    SOLVED_PUZZLE = np.arange(9).reshape((3, 3))

    # Constructor method that initalizes puzzle
    def __init__(self,conf,g,predState):
        self.puzzle = conf # PuzzleState
        self.gcost = g     # Cost of move
        self._compute_heuristic_cost() # Compute heuristic cost this sets hcost
        self.fcost = self.gcost + self.hcost
        self.pred = predState # Previous State
        self.zeroloc = np.argwhere(self.puzzle == 0)[0] # Sets location of blank tile as 0
        self.action_from_pred = None # Action we took to get to here up, down left right
    
    def __hash__(self):
        return tuple(self.puzzle.ravel()).__hash__() # Enables python to determine move is valid
    
    def _compute_heuristic_cost(self):
        """ Updates the heuristic function value for use in A* """
        # You have to use this to assign and return the hcost
    
    def is_goal(self):
        print(PuzzleState.SOLVED_PUZZLE) # DELETE
        print(self.puzzle) # DELETE
        return np.array_equal(PuzzleState.SOLVED_PUZZLE,self.puzzle)
    
    def __eq__(self, other):
        return np.array_equal(self.puzzle, other.puzzle)
    
    def __lt__(self, other): # Defines order of states. At each step we have options of next moves this defines the lowest cost move
        return self.fcost < other.fcost
    
    def __str__(self): # Enables you to print the puzzle state, and what to print
        #return np.str(self.puzzle)
        return np.str(self.puzzle) + ',gcost=' + str(gcost) + ',fcost=' + str(fcost)
    
    move = 0
    
    def show_path(self): # This shows us the path we just took
        if self.pred is not None:
            self.pred.show_path()
        
        if PuzzleState.move==0:
            print('START')
        else:
            print('Move',PuzzleState.move, 'ACTION:', self.action_from_pred)
        PuzzleState.move = PuzzleState.move + 1
        print(self)
    
    def can_move(self, direction):
        """ TODO """
        # Determines based on current state of current value of the blank tile location this detrmines if it can move up right down or left
        # if self.zeroloc is here in matrix it can go ->
        
    def gen_next_state(self, direction):
        """ TODO """
        # Get the next state of the puzzle based on the move

            

print('Artificial Intelligence')
print('MP1: A* for Sliding Puzzle')
print('SEMESTER: [put semester and year here]')
print('NAME: [your name here]')
print()

# In live lesson
frontier = queue.PriorityQueue()
a = np.loadtxt('mp1input.txt', dtype=np.int32)
start_state = PuzzleState(a,0,None)

frontier.put(start_state)

closed_set = set()

num_states = 0
while not frontier.empty():
    next_state = frontier.get() # This choses the best next state based on cost
    num_states = num_states + 1

    if next_state.is_goal():
        next_state.show_path()
        break
    
    closed_set.add(next_state)
    
    possible_moves = ['up','down','left','right']
    for move in possible_moves:
        if next_state.can_move(move):
            neighbor = next_state.gen_next_state(move) # return new state based on current state. ie the next move
            if neighbor in closed_set: # calls _hash_
                continue # closed set is all the states, this checks if the move is valid
            if neighbor not in frontier.queue:                           
                frontier.put(neighbor)

print('\nNumber of states visited =',num_states)

    