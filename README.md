# Maze Solving Algorithms

A comprehensive implementation and comparison of different maze-solving algorithms, including both informed and uninformed search methods.

## Algorithms Implemented

### Informed Search
- **A* Search (A*)**: Combines path cost and heuristic for optimal pathfinding
- **Greedy Best-First Search (GBFS)**: Uses heuristic to guide search towards goal

### Uninformed Search
- **Depth-First Search (DFS)**: Explores as far as possible along branches
- **Breadth-First Search (BFS)**: Explores all nodes at present depth
- **Iterative Deepening Search (IDS)**: Combines DFS's space efficiency with BFS's completeness

## Project Structure
```
Maze_Solving_Algorithms/
├── maze_solving/
│   ├── algorithms/        # Algorithm implementations
│   │   ├── __init__.py
│   │   ├── astar.py
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   ├── gbfs.py
│   │   └── ids.py
│   └── utils/            # Shared utility functions
│       └── __init__.py
├── visualization/        # Visualization and analysis tools
│   ├── __init__.py
│   ├── visualize_solution.py
│   ├── comparative_analysis.py
│   └── compare_algorithms.py
├── docs/                 # Documentation
│   └── images/          # Performance graphs and visualizations
├── tests/               # Test files
└── requirements.txt     # Project dependencies
```

## Features

- Implementation of 5 different maze-solving algorithms
- Comparative analysis of algorithms based on:
  - Number of expanded nodes
  - Time complexity (execution time)
  - Path cost from initial state to goal state
- Visual representation of maze solutions
- Performance metrics and statistics
- Customizable maze sizes and complexity

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Maze_Solving_Algorithms.git
cd Maze_Solving_Algorithms
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Visualize Individual Algorithm
```bash
python visualization/visualize_solution.py <algorithm> --size <maze_size> --loops <loop_percentage>
```
Example:
```bash
python visualization/visualize_solution.py astar --size 15 --loops 20
```

Available algorithms: astar, dfs, bfs, gbfs, ids

### Compare All Algorithms
```bash
python visualization/comparative_analysis.py
```
This will:
- Run all algorithms on different maze sizes
- Generate performance comparison graphs
- Print detailed metrics summary

### Performance Metrics
For each algorithm, you can view:
- Path Length: Number of steps from start to goal
- Execution Time: Time taken to find the solution
- Expanded Nodes: Number of nodes explored during search

## Dependencies
- Python 3.12+
- pyamaze>=1.0.0
- numpy>=1.21.0
- matplotlib>=3.4.0

## Contributing
Feel free to submit issues, fork the repository, and create pull requests for any improvements.
