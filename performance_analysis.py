import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from dijkstra import dijkstra

def main():

  N = [2**i for i in range(5, 14)]
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
  q_function=[]
  for ding in N:
    q_function.append(5.0e-7 * (ding**2) )


  fig, ax = plt.subplots(1,2, figsize=(15,5))

  ax[0].plot(N,T, label="Avg. execution time <T> vs graph size N")
  ax[0].plot(N,q_function, label='T=5.0E-7 N^2')
  ax[1].plot(np.log(N),np.log(T))
  ax[1].plot(np.log(N),np.log(q_function))
  ax[0].set(title='Avg. execution time <T> vs graph size N', xlabel='N', ylabel='<T> [s]')
  ax[1].set(title='Avg. execution time <T> vs graph size N', xlabel='log(N)', ylabel='log<T>')
  fig.legend()

  fig.tight_layout()

  plt.show()
  
if __name__ == "__main__":
  main()