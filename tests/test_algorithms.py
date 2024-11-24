import time
from pyamaze import maze
import sys
import os

# Add the parent directory to system path to import our package
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_maze_solving(size=10, algorithms=['dfs', 'bfs', 'astar', 'gbfs', 'ids']):
    """
    Test different maze solving algorithms and compare their performance.
    
    Args:
        size (int): Size of the maze (N x N)
        algorithms (list): List of algorithms to test
    """
    # Create a maze
    m = maze(size, size)
    m.CreateMaze(loopPercent=20)
    
    results = {}
    
    for algo in algorithms:
        print(f"\nTesting {algo.upper()} algorithm...")
        start_time = time.time()
        
        if algo == 'dfs':
            path = m.DFS
        elif algo == 'bfs':
            path = m.BFS
        elif algo == 'astar':
            path = m.AStar
        elif algo == 'gbfs':
            path = m.GBFS
        elif algo == 'ids':
            path = m.IDS
            
        end_time = time.time()
        execution_time = end_time - start_time
        
        path_length = len(path) if path else 0
        results[algo] = {
            'execution_time': execution_time,
            'path_length': path_length
        }
        
        print(f"Path length: {path_length}")
        print(f"Execution time: {execution_time:.4f} seconds")
        
        # Visualize the path
        m.tracePath({k: v for k, v in path.items()})
        m.run()
    
    return results

if __name__ == "__main__":
    # Test with different maze sizes
    sizes = [5, 10, 15]
    
    for size in sizes:
        print(f"\n=== Testing maze size {size}x{size} ===")
        results = test_maze_solving(size=size)
        
        # Print comparison
        print("\nAlgorithm Comparison:")
        print("-" * 50)
        print(f"{'Algorithm':<10} {'Path Length':<15} {'Time (s)':<10}")
        print("-" * 50)
        
        for algo, data in results.items():
            print(f"{algo.upper():<10} {data['path_length']:<15} {data['execution_time']:.4f}")
