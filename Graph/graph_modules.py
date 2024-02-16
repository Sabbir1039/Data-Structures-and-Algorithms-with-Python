from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def print_graph(self):
        for vertex, neigbours in self.graph.items():
            print(f"Vertex[{vertex}] : ", end="")
            for neigbour in neigbours:
                print(f" -> {neigbour}", end="")
            print('\n')
        
if __name__ == "__main__":
    graph = Graph()
    
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    
    graph.print_graph()
            

# Another one [not good for learning graph]

# implementation of graph using modules
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 2)
G.add_edge(2, 3)

# Display the graph
nx.draw(G, with_labels=True)
plt.show()
