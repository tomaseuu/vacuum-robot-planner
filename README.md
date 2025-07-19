# Vacuum Robot Planner (CSC 480 - Project 1)

This project implements a planner for the Vacuum World environment. The robot moves around a grid, vacuums dirty cells (*), avoids walls (#), and tries to clean everything.

**It uses two search algorithms:**
- **Uniform-Cost Search (UCS)** – always pick the cheapest path first, so it finds the shortest or best solution (priority queue)
- **Depth-First Search (DFS)** – keeps going down one path as far as it can before backtracking, so it is faster but does not always find the best solution

## How It Works
- The robot starts at @
- Dirty cells are *
- Blocked cells are #
- Empty cells are _
- The goal is to basically generate a sequence of moves to clean all dirty cells.
The robot can move North, South, East, or West, and it vacuums with V.

## How to Run
python3 planner.py [algorithm] [world-file.txt]
(ex: python3 planner.py depth-first test_worlds/sample-5x7.txt)

## How to Create worlds
Run: chmod +x make vacuum world . py
Next, use the example command on the bottom and customize it however you would like.
Example command: ./make_vacuum_world.py 5 7  0.15 3 > test_worlds/sample-5x7.txt  
(This generates a 5-row by 7-column world with approximately 15% blocked cells and 3
dirty cells, and saves it to sample-5x7.txt.)

**Algorithms:**
- depth-first
- uniform-cost

## Output Format
This program will print
- A list of actions: N, S, E, W, or V
- There are two lines that shows how many nodes were generated and expanded.

## Test Worlds I Used
I tested my code with a variety of maps:
- sample-3x3.txt
- sample-4x5.txt
- sample-5x7.txt
- sample-1x7.txt
- sample-2x2.txt
- sample-2x3.txt

## Important Notes
- Only accepts .txt files; anything else will show an error.
- If you forget an argument, it will tell you the correct way to write it.
- DFS avoids cycles, and UCS always returns the shortest path!
