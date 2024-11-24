"""
Comprehensive test suite for maze-solving algorithms.
Tests all algorithms on various maze sizes and validates their functionality.
"""

import os
import sys
import time
from pyamaze import maze

# Add the project root directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import all algorithms
from maze_solving.algorithms.astar import astar_search
from maze_solving.algorithms.gbfs import greedy_best_first_search
from maze_solving.algorithms.ids import iterative_deepening_search
from maze_solving.algorithms.ucs import uniform_cost_search

def test_algorithm(name, algo_func, maze_size=10, loop_percent=20):
    """Test a single algorithm on a maze of given size."""
    print(f"\nTesting {name} on {maze_size}x{maze_size} maze...")
    
    # Create maze
    m = maze(maze_size, maze_size)
    m.CreateMaze(loopPercent=loop_percent)
    
    # Run algorithm and time it
    start_time = time.time()
    path = algo_func(m)
    end_time = time.time()
    
    # Check results
    if path:
        print(f"✓ {name} found a path!")
        print(f"  Time taken: {end_time - start_time:.4f} seconds")
        print(f"  Path length: {len(path) + 1}")
        print(f"  Expanded nodes: {len(m.expanded_nodes)}")
        print(f"  Explored cells: {len(m.explored_cells)}")
        return True, {
            'time': end_time - start_time,
            'path_length': len(path) + 1,
            'expanded_nodes': len(m.expanded_nodes),
            'explored_cells': len(m.explored_cells)
        }
    else:
        print(f"✗ {name} failed to find a path!")
        return False, {}

def main():
    """Run comprehensive tests on all algorithms."""
    algorithms = {
        'A* Search': astar_search,
        'Greedy Best-First Search': greedy_best_first_search,
        'Uniform Cost Search': uniform_cost_search,
        'Iterative Deepening Search': iterative_deepening_search
    }
    
    maze_sizes = [10, 15, 20]  # Test different maze sizes
    results = {size: {} for size in maze_sizes}
    
    print("Starting comprehensive algorithm tests...")
    print("=" * 50)
    
    for size in maze_sizes:
        print(f"\nTesting on {size}x{size} maze")
        print("-" * 30)
        
        for name, algo in algorithms.items():
            success, metrics = test_algorithm(name, algo, size)
            if success:
                results[size][name] = metrics
    
    # Print summary
    print("\nTest Summary")
    print("=" * 50)
    
    for size in maze_sizes:
        print(f"\n{size}x{size} Maze Results:")
        print("-" * 30)
        for algo_name, metrics in results[size].items():
            print(f"\n{algo_name}:")
            print(f"  Time: {metrics['time']:.4f}s")
            print(f"  Path Length: {metrics['path_length']}")
            print(f"  Expanded Nodes: {metrics['expanded_nodes']}")
            print(f"  Explored Cells: {metrics['explored_cells']}")

if __name__ == "__main__":
    main()
