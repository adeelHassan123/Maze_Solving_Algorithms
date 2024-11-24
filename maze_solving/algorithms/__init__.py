"""
Maze solving algorithms package.
"""

from .astar import astar_search
from .gbfs import greedy_best_first_search
from .ids import iterative_deepening_search
from .ucs import uniform_cost_search

__all__ = [
    'astar_search',
    'greedy_best_first_search',
    'iterative_deepening_search',
    'uniform_cost_search'
]
