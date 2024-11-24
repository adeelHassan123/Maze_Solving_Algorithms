"""
Example script comparing different maze-solving algorithms.
"""

from pyamaze import maze
import time
import sys
import os

# Add the parent directory to system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from maze_solving.algorithms import (
    astar_search,
    depth_first_search,
    breadth_first_search,
    greedy_best_first_search,
    iterative_deepening_search
)

def compare_algorithms(maze_size=15, loop_percent=20):
    """Compare different maze-solving algorithms on the same maze."""
    # Create a single maze for all algorithms to ensure fair comparison
    m = maze(maze_size, maze_size)
    m.CreateMaze(loopPercent=loop_percent)
    
    algorithms = {
        'A*': astar_search,
        'DFS': depth_first_search,
        'BFS': breadth_first_search,
        'GBFS': greedy_best_first_search,
        'IDS': iterative_deepening_search
    }
    
    results = {}
    
    # Test each algorithm
    for name, algo in algorithms.items():
        print(f"\nTesting {name}...")
        
        # Run algorithm and measure time
        start_time = time.time()
        path = algo(m)
        end_time = time.time()
        
        # Store results
        results[name] = {
            'path_length': len(path),
            'time': end_time - start_time
        }
        
        print(f"Path length: {len(path)}")
        print(f"Time taken: {end_time - start_time:.4f} seconds")
    
    # Print comparison
    print("\nAlgorithm Comparison:")
    print("-" * 50)
    print(f"{'Algorithm':<10} {'Path Length':<15} {'Time (s)':<10}")
    print("-" * 50)
    
    for algo, data in results.items():
        print(f"{algo:<10} {data['path_length']:<15} {data['time']:.4f}")

if __name__ == "__main__":
    # Test with different maze sizes
    sizes = [5, 10, 15]
    
    for size in sizes:
        print(f"\n=== Testing maze size {size}x{size} ===")
        compare_algorithms(maze_size=size)
