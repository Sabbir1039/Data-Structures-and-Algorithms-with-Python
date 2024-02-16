# Graph (undirected) Adjacency List using dictionary representation in Python 
# space complexity of this implementation is O(V + E)
# time complexity of add_edge() is O(1) and print_graph() is O(V+E)

class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
    
    def add_edge(self, s, d) -> None:
        if s not in self.adj_list:
            self.adj_list[s] = []
        if d not in self.adj_list:
            self.adj_list[d] = []
        
        self.adj_list[s].append(d)
        self.adj_list[d].append(s)
        
    def print_graph(self) -> None:
        for index, list in self.adj_list.items():
            print(f"Vertex[{index}] : ", end="")
            for edge in list:
                print(f" -> {edge}", end="")
            print('\n')
    
if __name__ == "__main__":
    graph = Graph()
    
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    
    # print(graph.adj_list)
    
    graph.print_graph()