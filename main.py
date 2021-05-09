import networkx as nx
import matplotlib.pyplot as plt

def CreateGraph():
	G = nx.Graph()
	f = open('input.txt')
	n = int(f.readline())
	for i in range(n):
		graph_edge_list = f.readline().split()
		G.add_edge(graph_edge_list[0], graph_edge_list[1]) 
	return G

if __name__ == "__main__":
  G = CreateGraph()
  
  nx.draw_shell(G)
  plt.show()