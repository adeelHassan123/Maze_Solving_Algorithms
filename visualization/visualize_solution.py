"""
Script to visualize maze solutions using different algorithms.
"""

from pyamaze import maze, agent, textLabel
import sys
import os
import argparse
import time

# Add the parent directory to system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from maze_solving.algorithms import (
    astar_search,
    depth_first_search,
    breadth_first_search,
    greedy_best_first_search,
    iterative_deepening_search
)

def visualize_solution(algorithm, size=10, loop_percent=20):
    """
    Visualize a maze solution using the specified algorithm.
    
    Args:
        algorithm (str): Name of the algorithm to use ('astar', 'dfs', 'bfs', 'gbfs', 'ids')
        size (int): Size of the maze (N x N)
        loop_percent (int): Percentage of loops in the maze (0-100)
    """
    # Create maze
    m = maze(size, size)
    m.CreateMaze(loopPercent=loop_percent)
    
    # Map algorithm name to function
    algorithms = {
        'astar': astar_search,
        'dfs': depth_first_search,
        'bfs': breadth_first_search,
        'gbfs': greedy_best_first_search,
        'ids': iterative_deepening_search
    }
    
    if algorithm not in algorithms:
        print(f"Unknown algorithm: {algorithm}")
        print(f"Available algorithms: {', '.join(algorithms.keys())}")
        return
    
    # Get the path using selected algorithm
    start_time = time.time()
    path = algorithms[algorithm](m)
    execution_time = time.time() - start_time
    
    # Create an agent and visualize the path
    a = agent(m, footprints=True, filled=True)
    m.tracePath({a: path}, delay=100)
    
    # Add metrics as text labels
    textLabel(m, 'Algorithm', algorithm.upper())
    textLabel(m, 'Path Length', len(path))
    textLabel(m, 'Time', f'{execution_time:.4f}s')
    textLabel(m, 'Expanded Nodes', len(m.expanded_nodes) if hasattr(m, 'expanded_nodes') else 'N/A')
    textLabel(m, 'Explored Cells', len(m.explored_cells) if hasattr(m, 'explored_cells') else 'N/A')
    
    # Run the visualization
    m.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Visualize maze solutions.')
    parser.add_argument('algorithm', 
                      help='Algorithm to use (astar, dfs, bfs, gbfs, ids)')
    parser.add_argument('--size', type=int, default=10,
                      help='Size of the maze (default: 10)')
    parser.add_argument('--loops', type=int, default=20,
                      help='Percentage of loops in maze (default: 20)')
    
    args = parser.parse_args()
    visualize_solution(args.algorithm, args.size, args.loops)
