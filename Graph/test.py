class WeightedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj_list:
            self.adj_list[u] = {}
        if v not in self.adj_list:
            self.adj_list[v] = {}
        self.adj_list[u][v] = weight
        self.adj_list[v][u] = weight  # Uncomment if the graph is undirected

    def __str__(self):
        result = ""
        for vertex, neighbors in self.adj_list.items():
            result += f"{vertex}: {neighbors}\n"
        return result

# Example usage:
weighted_graph = WeightedGraph()
weighted_graph.add_edge('A', 'B', 5)
weighted_graph.add_edge('A', 'C', 3)
weighted_graph.add_edge('B', 'C', 2)
weighted_graph.add_edge('C', 'D', 7)
print(weighted_graph)
