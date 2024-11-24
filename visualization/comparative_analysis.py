"""
Comparative Analysis of Maze-Solving Algorithms.

This script compares uninformed (UCS, IDS) and informed (A*, GBFS) search methods
in terms of:
- Number of expanded nodes (nodes processed by the algorithm)
- Number of explored cells (cells seen during search)
- Time complexity (execution time)
- Path length from initial state to goal state
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

def run_analysis(maze_sizes=[10, 15, 20], trials=5):
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
        
        for trial in range(trials):
            print(f"  Trial {trial + 1}/{trials}")
            
            # Create maze
            m = maze(size, size)
            m.CreateMaze(loopPercent=20)
            
            # Test each algorithm
            for algo_name, (algo_func, is_informed) in algorithms.items():
                print(f"    Testing {algo_name}...")
                metrics = AlgorithmMetrics(algo_name, is_informed)
                
                # Measure execution time and get path
                start_time = time.time()
                path = algo_func(m)
                metrics.execution_time = time.time() - start_time
                
                if path:
                    # Record metrics
                    metrics.path_length = len(path) + 1  # +1 for start node
                    metrics.expanded_nodes = len(m.expanded_nodes)
                    metrics.explored_cells = len(m.explored_cells)
                    
                    # Store results
                    all_results[size][algo_name].append(metrics)
                else:
                    print(f"    Warning: {algo_name} failed to find a path!")
    
    return all_results

def plot_results(results):
    """Create visualizations of the analysis results."""
    maze_sizes = sorted(list(results.keys()))
    algo_names = list(results[maze_sizes[0]].keys())
    metrics = ['execution_time', 'path_length', 'expanded_nodes', 'explored_cells']
    titles = ['Execution Time (seconds)', 'Path Length', 'Expanded Nodes', 'Explored Cells']
    y_labels = ['Time (s)', 'Length', 'Number of Nodes', 'Number of Cells']
    
    # Set style for better visibility
    plt.style.use('default')
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    
    # Create a figure with four subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Maze-Solving Algorithm Comparison', fontsize=16, y=1.02)
    axes = axes.flatten()
    
    # Colors for different algorithms
    colors = ['#2ecc71', '#e74c3c', '#3498db', '#f1c40f']
    
    for idx, (metric, title, ylabel) in enumerate(zip(metrics, titles, y_labels)):
        ax = axes[idx]
        
        # Prepare data for plotting
        data = {algo: [] for algo in algo_names}
        errors = {algo: [] for algo in algo_names}
        
        for size in maze_sizes:
            for algo in algo_names:
                # Calculate average and standard deviation over trials
                values = [getattr(m, metric) for m in results[size][algo]]
                data[algo].append(np.mean(values))
                errors[algo].append(np.std(values))
        
        # Plot lines with error bands
        for algo, color in zip(algo_names, colors):
            ax.plot(maze_sizes, data[algo], marker='o', label=algo, color=color, linewidth=2)
            ax.fill_between(maze_sizes,
                          np.array(data[algo]) - np.array(errors[algo]),
                          np.array(data[algo]) + np.array(errors[algo]),
                          alpha=0.2, color=color)
        
        ax.set_xlabel('Maze Size (N×N)', fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.set_title(title, fontsize=12, pad=10)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(title='Algorithms', title_fontsize=10)
        
        # Add minor gridlines
        ax.minorticks_on()
        ax.grid(which='minor', linestyle=':', alpha=0.4)
    
    # Adjust layout and save
    plt.tight_layout()
    
    # Create docs/images directory if it doesn't exist
    os.makedirs('docs/images', exist_ok=True)
    
    # Save the plot
    plt.savefig('docs/images/algorithm_comparison.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as 'docs/images/algorithm_comparison.png'")

def print_summary(results):
    """Print a detailed summary of the analysis results."""
    print("\nAnalysis Summary")
    print("=" * 80)
    
    for size in sorted(results.keys()):
        print(f"\nMaze Size: {size}x{size}")
        print("-" * 40)
        
        for algo in results[size]:
            metrics = results[size][algo]
            avg_time = np.mean([m.execution_time for m in metrics])
            avg_path = np.mean([m.path_length for m in metrics])
            avg_expanded = np.mean([m.expanded_nodes for m in metrics])
            avg_explored = np.mean([m.explored_cells for m in metrics])
            
            print(f"\n{algo}:")
            print(f"  Average Time: {avg_time:.4f}s")
            print(f"  Average Path Length: {avg_path:.1f}")
            print(f"  Average Expanded Nodes: {avg_expanded:.1f}")
            print(f"  Average Explored Cells: {avg_explored:.1f}")

if __name__ == "__main__":
    print("Running comparative analysis...")
    print("This may take a few minutes...")
    
    # Run analysis
    results = run_analysis()
    
    # Generate visualizations
    plot_results(results)
    
    # Print summary
    print_summary(results)
    
    print("\nAnalysis complete!")
