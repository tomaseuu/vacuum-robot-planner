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

# Depth-First-Search (Last In first Out)

def dfs (robot_pos, dirty_cells, grid):
     visited = set() #empty set instead of list
     stack = [((robot_pos, dirty_cells), [])]

     nodes_generated = 0
     nodes_expanded = 0

     while stack:
          (position, dirty_cells_left), path = stack.pop()
          nodes_expanded += 1

          state_key = (position, tuple(sorted(dirty_cells_left)))

          if state_key in visited:
               continue
          visited.add(state_key)

          if not dirty_cells_left:
               for action in path:
                    print(action)
               print(f"{nodes_generated}: nodes generated")
               print(f"{nodes_expanded}: nodes expanded")
               return path
          if dirty_cells_left:
               new_dirty = set(dirty_cells_left)
               new_dirty.remove(position) # remove this position from the set of dirty cells since vacuumed.
               stack.append(((position, new_dirty), path + ['V']))
               nodes_generated += 1
               continue
          

          direction_map = {
               'N':(-1,0), # up
               'S':(1,0), # down
               'E':(0,1), # right
               'W':(0,-1), # left
          }

          for action, (delta_row, delta_col) in direction_map.items():
               new_row = position[0] + delta_row
               new_col = position[1] + delta_col

               if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]): #grids bound
                    if grid[new_row][new_col] != "#":
                         new_position = (new_row, new_col)
                         stack.append(((new_position, dirty_cells_left), path + [action]))
                         nodes_generated += 1

     print("no plan found")
     return None


'''
print("Grid:")
for row in grid:
    print("".join(row))

print("\nRobot Position:", robot_pos)
print("Dirty Cells:", dirty_cells)
print("Blocked Cells:", blocked_cells)
print("Empty Cells:", empty_cells)
'''