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

from maze_solving.algorithms.astar import astar_search
from maze_solving.algorithms.gbfs import greedy_best_first_search
from maze_solving.algorithms.ids import iterative_deepening_search
from maze_solving.algorithms.ucs import uniform_cost_search

def visualize_solution(algorithm, size=10, loop_percent=20):
    """
    Visualize a maze solution using the specified algorithm.
    
    Args:
        algorithm (str): Name of the algorithm to use ('astar', 'ucs', 'gbfs', 'ids')
        size (int): Size of the maze (N x N)
        loop_percent (int): Percentage of loops in the maze (0-100)
    """
    # Create maze
    m = maze(size, size)
    m.CreateMaze(loopPercent=loop_percent)
    
    # Map algorithm name to function
    algorithms = {
        'astar': astar_search,
        'ucs': uniform_cost_search,
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
    end_time = time.time()
    
    if not path:
        print(f"No solution found using {algorithm}!")
        return
    
    # Create agent and add path trace
    a = agent(m, footprints=True, shape='arrow')
    m.tracePath({a: path})
    
    # Add metrics labels
    l = textLabel(m, 'Algorithm', algorithm.upper())
    l = textLabel(m, 'Path Length', len(path) + 1)
    l = textLabel(m, 'Time', f'{(end_time-start_time):.4f}s')
    l = textLabel(m, 'Expanded Nodes', len(m.expanded_nodes))
    l = textLabel(m, 'Explored Cells', len(m.explored_cells))
    
    # Run visualization
    m.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Visualize maze solutions.')
    parser.add_argument('--algorithm', 
                      help='Algorithm to use (astar, ucs, gbfs, ids)',
                      required=True,
                      choices=['astar', 'ucs', 'gbfs', 'ids'])
    parser.add_argument('--size',
                      help='Size of the maze (N x N)',
                      type=int,
                      default=10)
    parser.add_argument('--loops',
                      help='Percentage of loops in maze (0-100)',
                      type=int,
                      default=20)
    
    args = parser.parse_args()
    visualize_solution(args.algorithm, args.size, args.loops)
