"""
Comparative Analysis of Maze-Solving Algorithms.

This script compares uninformed (DFS, BFS, IDS) and informed (A*, GBFS) search methods
in terms of:
- Number of expanded nodes
- Time complexity (execution time)
- Path cost from initial state to goal state
"""

import sys
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from pyamaze import maze
from collections import defaultdict

# Add the parent directory to system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from maze_solving.algorithms.astar import astar_search
from maze_solving.algorithms.gbfs import greedy_best_first_search
from maze_solving.algorithms.ids import iterative_deepening_search
from maze_solving.algorithms.ucs import uniform_cost_search

class AlgorithmMetrics:
    def __init__(self, name, is_informed):
        self.name = name
        self.is_informed = is_informed
        self.expanded_nodes = 0
        self.explored_cells = 0
        self.execution_time = 0
        self.path_length = 0

def run_analysis(maze_sizes=[5, 10, 15, 20], trials=3):
    """Run comparative analysis on different maze sizes."""
    algorithms = {
        'UCS': (uniform_cost_search, False),
        'IDS': (iterative_deepening_search, False),
        'GBFS': (greedy_best_first_search, True),
        'A*': (astar_search, True)
    }
    
    all_results = defaultdict(lambda: defaultdict(list))
    
    for size in maze_sizes:
        print(f"\nAnalyzing maze size: {size}x{size}")
        
        for _ in range(trials):
            # Create maze
            m = maze(size, size)
            m.CreateMaze(loopPercent=20)
            
            # Test each algorithm
            for algo_name, (algo_func, is_informed) in algorithms.items():
                metrics = AlgorithmMetrics(algo_name, is_informed)
                
                # Measure execution time and get path
                start_time = time.time()
                path = algo_func(m)
                metrics.execution_time = time.time() - start_time
                
                # Record metrics
                metrics.path_length = len(path)
                metrics.expanded_nodes = len(m.expanded_nodes) if hasattr(m, 'expanded_nodes') else 0
                metrics.explored_cells = len(m.explored_cells) if hasattr(m, 'explored_cells') else 0
                
                # Store results
                all_results[size][algo_name].append(metrics)
    
    return all_results

def plot_results(results):
    """Create visualizations of the analysis results."""
    maze_sizes = list(results.keys())
    algo_names = list(results[maze_sizes[0]].keys())
    metrics = ['execution_time', 'path_length', 'expanded_nodes', 'explored_cells']
    titles = ['Execution Time', 'Path Length', 'Expanded Nodes', 'Explored Cells']
    
    # Create a figure with four subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Maze-Solving Algorithm Comparison')
    axes = axes.flatten()
    
    for idx, (metric, title) in enumerate(zip(metrics, titles)):
        ax = axes[idx]
        
        # Prepare data for plotting
        data = {algo: [] for algo in algo_names}
        for size in maze_sizes:
            for algo in algo_names:
                # Calculate average over trials
                avg_value = np.mean([getattr(m, metric) for m in results[size][algo]])
                data[algo].append(avg_value)
        
        # Plot lines
        for algo in algo_names:
            ax.plot(maze_sizes, data[algo], marker='o', label=algo)
        
        ax.set_xlabel('Maze Size')
        ax.set_ylabel(title)
        ax.grid(True)
        ax.legend()
    
    plt.tight_layout()
    plt.savefig('docs/images/algorithm_comparison.png')
    plt.close()

def print_summary(results):
    """Print a summary of the analysis results."""
    print("\nComparative Analysis Summary")
    print("=" * 80)
    
    for size in results:
        print(f"\nMaze Size: {size}x{size}")
        print("-" * 30)
        print(f"{'Algorithm':<10} {'Time (s)':<12} {'Path Length':<12} {'Expanded':<12} {'Explored':<12}")
        print("-" * 80)
        
        for algo in results[size]:
            metrics = results[size][algo]
            avg_time = np.mean([m.execution_time for m in metrics])
            avg_path = np.mean([m.path_length for m in metrics])
            avg_expanded = np.mean([m.expanded_nodes for m in metrics])
            avg_explored = np.mean([m.explored_cells for m in metrics])
            
            print(f"{algo:<10} {avg_time:<12.4f} {avg_path:<12.1f} {avg_expanded:<12.1f} {avg_explored:<12.1f}")

if __name__ == "__main__":
    # Run analysis
    results = run_analysis()
    
    # Generate visualizations
    plot_results(results)
    
    # Print summary
    print_summary(results)
