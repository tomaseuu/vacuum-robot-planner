import sys
import random
import heapq


# run this to test:  python3 planner.py depth-first test_worlds/sample-5x7.txt
# Read .txt and extract it
file_path = sys.argv[2]
with open(file_path, 'r') as f:
     lines = f.readlines()

columns = int(lines[0])
rows = int(lines[1])
grid = []
for line in lines [2:]:
     clean_line = line.strip() # remove the \n
     row_characters = list(clean_line) # breaks string into a list of characters
     grid.append(row_characters)

'''
grid reprsentation.

- = empty cell
# = blocked cell
* = dirty cell
@ = robot starting location


dirty cells: {(1,4), (2,2), (3,4)} from that example
____###
____*__
__*____
____*#@
___#___


'''
# set over list
#.  - no duplicates allowed
#.  - order is not important

robot_pos = None # no (0,0) cause it could start at different positions
dirty_cells = set()
blocked_cells = set()
empty_cells = set()

# NEVER UP AND DOWN, it is always left to right or right to left (tip)
for r in range(rows): # top to bot row
     for c in range(columns): # left to right
          cell = grid[r][c]
          if cell == '@' :
               robot_pos = (r,c)
          elif cell == '*':
               dirty_cells.add((r,c))
          elif cell == '#':
               blocked_cells.add((r,c))
          elif cell == '_':
               empty_cells.add((r,c))
