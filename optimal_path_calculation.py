import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from dijkstra import dijkstra

def main():
  # Init empty graph
  G = nx.DiGraph()

  # Open edgelist file
  with open("edgelist.txt") as f:
    entries = f.readlines()
    edges = []
    # Convert entries (lines) to networkx edge format
    for entry in entries:
      edge = entry.split(',')
      edge[2] = int(edge[2])
      edges.append(edge)
    print(edges)
    # Add edges to graph
    G.add_weighted_edges_from(edges)
    
  # Find path requested by the user
  origin = input("Enter the origin node: ")
  destination = input("Enter the destination node: ")
  path = dijkstra(G, origin, destination)
  print(f"The shortest path from {origin} to {destination} is ", "->".join(path))

if __name__ == "__main__":
  main()