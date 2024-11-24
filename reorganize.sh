#!/bin/bash

# Create new directory
mkdir -p visualization

# Move files from examples to visualization
mv examples/visualize_solution.py visualization/visualize_solution.py
mv examples/comparative_analysis.py visualization/comparative_analysis.py
mv examples/compare_algorithms.py visualization/compare_algorithms.py

# Remove old directory
rm -rf examples

# Create visualization/__init__.py
touch visualization/__init__.py
