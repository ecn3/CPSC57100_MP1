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

puzzle_input = np.loadtxt('mp1input.txt', dtype=np.int32)

# Output
print('Artificial Intelligence')
print('MP1: A* for Sliding Puzzle')
print('SEMESTER: Fall 2020')
print('NAME: Christian Nelson')
print("")

print("START")
print(puzzle_input)

#print(move_fmt.format("1","right"))

# Get current location of 0
print(np.argwhere(puzzle_input == 0)[0] )
