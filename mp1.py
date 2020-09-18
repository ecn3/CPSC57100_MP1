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

SOLVED_PUZZLE = np.arange(9).reshape((3, 3))

# Current locations
loc_of_0_current = np.argwhere(puzzle_input == 0)[0]
loc_of_1_current = np.argwhere(puzzle_input == 1)[0]
loc_of_2_current = np.argwhere(puzzle_input == 2)[0]
loc_of_3_current = np.argwhere(puzzle_input == 3)[0]
loc_of_4_current = np.argwhere(puzzle_input == 4)[0]
loc_of_5_current = np.argwhere(puzzle_input == 5)[0]
loc_of_6_current = np.argwhere(puzzle_input == 6)[0]
loc_of_7_current = np.argwhere(puzzle_input == 7)[0]
loc_of_8_current = np.argwhere(puzzle_input == 8)[0]

loc_of_0_goal = np.argwhere(SOLVED_PUZZLE == 0)[0]
loc_of_1_goal = np.argwhere(SOLVED_PUZZLE == 1)[0]
loc_of_2_goal = np.argwhere(SOLVED_PUZZLE == 2)[0]
loc_of_3_goal = np.argwhere(SOLVED_PUZZLE == 3)[0]
loc_of_4_goal = np.argwhere(SOLVED_PUZZLE == 4)[0]
loc_of_5_goal = np.argwhere(SOLVED_PUZZLE == 5)[0]
loc_of_6_goal = np.argwhere(SOLVED_PUZZLE == 6)[0]
loc_of_7_goal = np.argwhere(SOLVED_PUZZLE == 7)[0]
loc_of_8_goal = np.argwhere(SOLVED_PUZZLE == 8)[0]

print("current: ")
print(
"0",loc_of_0_current,
"1",loc_of_1_current,
"2",loc_of_2_current,
"3",loc_of_3_current,
"4",loc_of_4_current,
"5",loc_of_5_current,
"6",loc_of_6_current,
"7",loc_of_7_current,
"8",loc_of_8_current
)

print("Goal: ")
print(
"0",loc_of_0_goal,
"1",loc_of_1_goal,
"2",loc_of_2_goal,
"3",loc_of_3_goal,
"4",loc_of_4_goal,
"5",loc_of_5_goal,
"6",loc_of_6_goal,
"7",loc_of_7_goal,
"8",loc_of_8_goal
)

man_0 = abs(loc_of_0_current[0] - loc_of_0_goal[0]) + abs(loc_of_0_current[1] - loc_of_0_goal[1])

print(man_0)