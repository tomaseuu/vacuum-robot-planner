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
     row_characters = list(clean_line)
     grid.append(row_characters)
print(grid)
    
