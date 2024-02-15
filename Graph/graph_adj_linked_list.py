# Adjascency List using linked list representation in Python
class AdjNode:
    def __init__(self, value) -> None:
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, num) -> None:
        self.V_num = num # num of vertex in graph
        self.graph = [None] * self.V_num  # [None] *3 = [None, None, None]
    
    def add_edge(self, source, dest) -> None:
        node = AdjNode(dest)
        node.next = self.graph[source]
        self.graph[source] = node
        
        node = AdjNode(source)
        node.next = self.graph[dest]
        self.graph[dest] = node
        
    def print_graph(self):
        for i in range(self.V_num):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print("\n")

if __name__ == "__main__":
    V = 4 # number of vertex

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_graph()
    
    # result
    # Vertex 0: -> 3 -> 2 -> 1
    # Vertex 1: -> 2 -> 0     
    # Vertex 2: -> 1 -> 0
    # Vertex 3: -> 0