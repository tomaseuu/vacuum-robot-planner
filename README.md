# Vacuum Robot Planner (CSC 480 - Project 1)

This project implements a planner for the Vacuum World environment using two search algorithms:
- **Uniform-Cost Search (UCS)** – always pick the cheapest path first, so it finds the shortest or best solution (priority queue)
- **Depth-First Search (DFS)** – keeps going down one path as far as it can before backtracking, so it is faster but does not always find the best solution

## How to Run

In terminal:
python3 planner.py [algorithm] [world-file]
