# EEX02 Project 0
By Kenneth Laban (6099718), Christopher Kusumo (6001378), Lana Boers (5545544).

## Compilation Instructions
To compile the code, one only needs to run the program using the python command in the terminal. The project relies on the following external libraries as dependencies:
- NetworkX
- NumPy
- Matplotlib
These libraries need to be installed in order for the code to function properly.

The project contains three files. One file, dijkstra.py, contains the function that runs the Dijkstra algorithm itself. This file is not intended to run by itself.

The second file, optimal_path_calculation.py, uses the Dijkstra algorithm to find the shortest path between two nodes in a user-specified graph. This file reads a textfile edgelist.txt, to be supplied by the user, in order to generate the graph. The edgelist.txt file needs to be formatted in a specific way: each edge requires its own line in the format "node1,node2,weight". An example is supplied with the project code for reference.

The third file, performance_analysis.py, runs the performance analysis on Erdős Rényi graphs. This file does not require any user intervention.
