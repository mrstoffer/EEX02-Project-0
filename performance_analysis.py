import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from dijkstra import dijkstra

def main():

  N = [2**i for i in range(5,14)]
  k = 20

  T = []

  for n in N:
    p = n / k
    er = nx.erdos_renyi_graph(n,p, seed=None, directed=False, create_using=None)
    for u, v in er.edges():
      er[u][v]['weight'] = 1 
    
    t = []
    
    print(np.log2(n))
    
    for m in range(20):
      er_org = random.choice(list(er.nodes))
      er_dest = random.choice(list(er.nodes))
      
      # print(er_org, er_dest)
      
      start = time.time()
      er_path = dijkstra(er, er_org, er_dest)
      end = time.time()
      
      t.append(end-start)
    
    T.append((1/(m+1))*sum(t))
    
  with open("results/results.txt", "w") as f:
    f.write(N)
    f.write("\n")
    f.write(T)

  fig, ax = plt.subplots(1,2, figsize=(15,5))

  ax[0].plot(N,T)
  ax[1].plot(np.log(N),np.log(T))

  ax[0].set(title='Avg. execution time <T> vs graph size N', xlabel='N', ylabel='<T> [s]')
  ax[1].set(title='Avg. execution time <T> vs graph size N', xlabel='log(N)', ylabel='log<T>')

  fig.tight_layout()

  plt.show()
  
if __name__ == "__main__":
  main()