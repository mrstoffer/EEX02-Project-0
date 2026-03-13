import networkx as nx
import numpy as np

def dijkstra(G, source, destination):
  # Initialization: set distances (labels) for all nodes to infinity except for the source node
  distances = {node: np.inf for node in G.nodes()}
  distances[source] = 0
  predecessors = {node: None for node in G.nodes()}
  
  # Keep track of unvisited nodes (temporary labels)
  unvisited = list(G.nodes())
  while unvisited: # iterate until every node is checked
    current_node = min(unvisited, key=lambda node: distances[node]) # choose the closest unvisited node from the source
    
    if distances[current_node] == np.inf: # break if the closest unvisited node still has infinite distance to the source
      break
    
    unvisited.remove(current_node) # remove the current node from the unvisited
    
    for neighbor in G.neighbors(current_node): # check the distances from current node to neighbors
      weight = G[current_node][neighbor]['weight']
      new_dist = distances[current_node] + weight
      if new_dist < distances[neighbor]:
        distances[neighbor] = new_dist
        predecessors[neighbor] = current_node
  
  # Find path to the node by tracing back all predecessors from the destination
  path = []
  next_node = destination
  while next_node is not None:
    path.append(next_node)
    next_node = predecessors[next_node]
  path.reverse()
  
  if path[0] == source:
    return path
  else:
    # No path to the source could be found
    return []