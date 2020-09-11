""" 
Christian Nelson
9/11/2020
CPSC-57100-002, Fall 2020
Machine Problem 1: Sliding Puzzle
"""

# Imports
import numpy as np
import queue
#from multiprocessing import Queue

# Output Heading
print('Artificial Intelligence')
print('MP1: A* for Sliding Puzzle')
print('SEMESTER: Fall 2020')
print('NAME: Christian Nelson')
print("")

# load random start state onto frontier priority queue
frontier = queue.PriorityQueue()