import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import time

# input: [(edge 1, edge 2, weight)]
def dijkstra(G, origin, destination):
  labels = {}
  predecessors = {}
  for node in G.nodes:
    labels[node] = np.inf
    predecessors[node] = None
  # print(labels)
  current_node = origin
  labels[current_node] = 0
  visited_nodes = []
  current_label = 0
  while True:
    for neighbour in G.neighbors(current_node):
      if (labels[neighbour] > current_label+G[current_node][neighbour]["weight"]):
        labels[neighbour] = current_label+G[current_node][neighbour]["weight"]
        predecessors[neighbour] = current_node
        
    visited_nodes.append(current_node)
    filtered_labels = {node: label for node, label in labels.items() if node not in visited_nodes}
    current_node = min(filtered_labels, key=labels.get)
    current_label = labels[current_node]
    
    if current_node == destination:
      break
    
  # print(labels)
  # print(predecessors)
  
  if labels[destination] == np.inf:
    return []
  
  path = [destination]
  next_node = predecessors[destination]
  while (next_node != origin and next_node is not None  ):
    path.append(next_node)
    next_node = predecessors[next_node]
  path.append(origin)
  path.reverse()
  return path


G = nx.DiGraph()
G.add_weighted_edges_from([('S', 'D', 8), ('S', 'E', 1), ('D', 'C', 3), ('E', 'C', 1), ('B', 'D', 2), ('C', 'A', 2), ('A', 'B', 1), ('B', 'H', 1), ('A', 'F', 5), ('F', 'H', 3), ('F', 'G', 1), ('H', 'G', 1), ('G', 'E', 1)])
path = dijkstra(G, 'S', 'G')
print(path)

N = [2**i for i in range(5,14)]
k = 20

T = []

for n in N:
  p = n / k
  er = nx.erdos_renyi_graph(n,p, seed=None, directed=False, create_using=None)
  for u, v in er.edges():
    er[u][v]['weight'] = 1 
  
  t = []
  
  for m in range(20):
    er_org = random.choice(list(er.nodes))
    er_dest = random.choice(list(er.nodes))
    
    # print(er_org, er_dest)
    
    start = time.time()
    er_path = dijkstra(er, er_org, er_dest)
    end = time.time()
    
    t.append(end-start)
  
  T.append((1/m)*sum(t))

fig, ax = plt.subplots(1,2, figsize=(15,5))

ax[0].plot(N,T)
ax[1].semilogy(N,T)

ax[0].set(title='Avg. execution time <T> vs graph size N', xlabel='N', ylabel='<T> [s]')
ax[1].set(title='Avg. execution time <T> vs graph size N', xlabel='x', ylabel='log<T>')

fig.tight_layout()

plt.show()
    
    
  
# nx.draw(G, with_labels=True)
# plt.show()