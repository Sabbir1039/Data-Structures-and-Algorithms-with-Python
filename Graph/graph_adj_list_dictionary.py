from collections import defaultdict

class Graph:
    def __init__(self, vertices: list[str]) -> None:
        if not vertices:
            raise ValueError("vertices list can not be empty")
        if len(vertices) != len(set(vertices)):
            raise ValueError(f"All vertex names must be unique")
        
        self.vertices_count = len(vertices)
        self.adj_list = defaultdict(list)
        self.vertices_set = set(vertices)


    def _valid_vertex(self, vertex: str) -> None:
        if not vertex in self.vertices_set:
            raise KeyError(f"Vertex '{vertex}' does not exist in the graph")
    

    def add_edge(self, vertex_i: str, vertex_j: str, weight: int = 1) -> None:
        self._valid_vertex(vertex_i)
        self._valid_vertex(vertex_j)

        self.adj_list[vertex_i].append((vertex_j, weight))
        self.adj_list[vertex_j].append((vertex_i, weight))
    
    def print_graph(self):
        print(f"Vertex : Neighbours...")
        print("=" * 50)
        for vertex, neighbours in self.adj_list.items():
            print(f"{vertex} : ", end="")
            for v in neighbours:
                print(v, end=" ")
            print() 

if __name__ == "__main__":
    nodes = ["A", "B", "C", "D"]
    g = Graph(nodes)

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.add_edge("C", "D")

    g.print_graph()