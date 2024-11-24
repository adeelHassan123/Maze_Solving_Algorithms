# Maze Solving Algorithms

This project implements and compares different maze-solving algorithms, focusing on both informed and uninformed search strategies.

## Implemented Algorithms

### Uninformed Search
- Uniform Cost Search (UCS)
- Iterative Deepening Search (IDS)

### Informed Search
- Greedy Best-First Search (GBFS)
- A* Search (with Manhattan distance heuristic)

## Project Structure

```
maze_solving/
├── algorithms/
│   ├── astar.py      # A* Search implementation
│   ├── gbfs.py       # Greedy Best-First Search implementation
│   ├── ids.py        # Iterative Deepening Search implementation
│   └── ucs.py        # Uniform Cost Search implementation
└── utils/
    └── __init__.py   # Utility functions

visualization/
├── comparative_analysis.py  # Compare algorithm performance
├── compare_algorithms.py    # Generate comparison graphs
└── visualize_solution.py    # Visualize individual solutions

docs/
└── images/                 # Performance graphs and visualizations
```

## Features

- Implementation of 4 different maze-solving algorithms
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
python visualization/visualize_solution.py --algorithm [ucs|ids|gbfs|astar]
```
Example:
```bash
python visualization/visualize_solution.py --algorithm astar
```

Available algorithms: ucs, ids, gbfs, astar

### Compare All Algorithms
```bash
python visualization/comparative_analysis.py
```
This will:
- Run all algorithms on different maze sizes
- Generate performance comparison graphs
- Print detailed metrics summary

## Performance Metrics

Each algorithm tracks:
- Expanded nodes (nodes processed by the algorithm)
- Explored cells (cells seen during search)
- Execution time
- Path length

## Results

The algorithms are compared across different maze sizes (10x10, 15x15, 20x20) on metrics including:
- Number of expanded nodes
- Number of explored cells
- Execution time
- Path length

See generated graphs in `docs/images/` for detailed comparisons.

## Dependencies
- Python 3.12+
- pyamaze>=1.0.0
- numpy>=1.21.0
- matplotlib>=3.4.0

## Contributing
Feel free to submit issues, fork the repository, and create pull requests for any improvements.
