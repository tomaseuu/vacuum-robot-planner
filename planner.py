import sys
import heapq

'''
--------------------------------------------------------------------
Assignment 1: Vacuum Robot Planner
DFS & UCS implementation

Program must be able to read a .txt file containing a grid world.
3
3
_@_
___
__*
 + Line 1: Number of Columns
 + Line 2: Number of Rows
 + Remaining Lines: one row per line from top to bottom

Each character represnts a cell:
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

Commands to run the testworlds (copy and paste)
--
python3 planner.py depth-first test_worlds/sample-5x7.txt
python3 planner.py uniform-cost test_worlds/sample-5x7.txt
--
python3 planner.py depth-first test_worlds/sample-1x7.txt
python3 planner.py uniform-cost test_worlds/sample-1x7.txt
--
python3 planner.py depth-first test_worlds/sample-2x2.txt
python3 planner.py uniform-cost test_worlds/sample-2x2.txt
--
python3 planner.py depth-first test_worlds/sample-2x3.txt
python3 planner.py uniform-cost test_worlds/sample-2x3.txt
--
python3 planner.py depth-first test_worlds/sample-3x3.txt
python3 planner.py uniform-cost test_worlds/sample-3x3.txt
--
python3 planner.py depth-first test_worlds/sample-4x5.txt
python3 planner.py uniform-cost test_worlds/sample-4x5.txt
--------------------------------------------------------------------
'''



#  Depth-First Search (DFS) 
def dfs (robot_pos, dirty_cells, grid):
     visited = set() 
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

          # Goal check
          if not dirty_cells_left:
               for action in path:
                    print(action)
               print(f"{nodes_generated} nodes generated")
               print(f"{nodes_expanded} nodes expanded")
               return path
          
          # Vacuum current cell
          if position in dirty_cells_left:
               new_dirty = set(dirty_cells_left)
               new_dirty.remove(position)
               stack.append(((position, new_dirty), path + ['V']))
               nodes_generated += 1
               continue
          
          # All directions
          direction_map = {
               'N':(-1,0), # up
               'S':(1,0), # down
               'E':(0,1), # right
               'W':(0,-1), # left
          }

          for action, (delta_row, delta_col) in direction_map.items():
               new_row = position[0] + delta_row
               new_col = position[1] + delta_col

               if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    if grid[new_row][new_col] != "#":
                         new_position = (new_row, new_col)
                         stack.append(((new_position, dirty_cells_left), path + [action]))
                         nodes_generated += 1

     print("no plan found")
     return None

# Uniform Cost Search (Priority queue)
def ucs(robot_pos, dirty_cells, grid):
     visited = set()
     fringe = [(0,(robot_pos, dirty_cells), [])] 

     nodes_generated = 0
     nodes_expanded = 0

     while fringe:
          cost, (position, dirty_cells_left), path = heapq.heappop(fringe)
          nodes_expanded +=1

          state_key = (position, tuple(sorted(dirty_cells_left)))

          if state_key in visited:
               continue
          visited.add(state_key)

          # Goal check
          if not dirty_cells_left:
               for action in path:
                    print(action)
               print(f"{nodes_generated} nodes generated")
               print(f"{nodes_expanded} nodes expanded")
               return path
          # Vacuum current cell
          if position in dirty_cells_left:
               new_dirty = set(dirty_cells_left)
               new_dirty.remove(position)
               heapq.heappush(fringe, (cost + 1, (position, new_dirty), path + ['V']))
               nodes_generated += 1
               continue
          
          # All directions
          direction_map = {
               'N':(-1,0), # up
               'S':(1,0), # down
               'E':(0,1), # right
               'W':(0,-1), # left
          }

          for action, (delta_row, delta_col) in direction_map.items():
               new_row = position[0] + delta_row
               new_col = position[1] + delta_col

               if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    if grid[new_row][new_col] != "#":
                         new_position = (new_row, new_col)
                         heapq.heappush(fringe, (cost + 1, (new_position, dirty_cells_left), path + [action]))
                         nodes_generated += 1
     print("no plan found")
     return None

# Main Program
if __name__ == "__main__":
     # Check to make sure command-line arguments are true
     if len(sys.argv) != 3:
          print("Please Write this: python3 planner.py [depth-first|uniform-cost] [world-file.txt]")
          sys.exit(1)
     method = sys.argv[1]
     file_path = sys.argv[2]

     if not file_path.endswith(".txt"):
          print("error: world file must be a .txt file.")
          sys.exit(1)

     # Read world file
     with open(file_path, 'r') as f:
          lines = f.readlines()

     columns = int(lines[0])
     rows = int(lines[1])
     grid = []
     for line in lines [2:]:
          clean_line = line.strip() 
          row_characters = list(clean_line)
          grid.append(row_characters)

     # Extract robot, dirt, and obstacles
     robot_pos = None
     dirty_cells = set()
     blocked_cells = set()
     empty_cells = set()

     for r in range(rows): 
          for c in range(columns): 
               cell = grid[r][c]
               if cell == '@' :
                    robot_pos = (r,c)
               elif cell == '*':
                    dirty_cells.add((r,c))
               elif cell == '#':
                    blocked_cells.add((r,c))
               elif cell == '_':
                    empty_cells.add((r,c))

     # Run selected search method
     if method == "depth-first":
          dfs(robot_pos, dirty_cells, grid)
     elif method == "uniform-cost":
          ucs(robot_pos, dirty_cells, grid)
     else:
          print(f"unknown method: {method}")
