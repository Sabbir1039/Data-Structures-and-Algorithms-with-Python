class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
        
    def add_edge(self, u, v) -> None:
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    
    # The time complexity for the BFS traversal itself is O(V + E)
    def bfs(self, source) -> None:
        que = []
        visited = [False] * len(self.adj_list)
        que.append(source)
        visited[source] = True
        
        while que:
            front_v = que.pop(0)
            print(f"{front_v }", end=" ")
            
            for neighbour in self.adj_list[front_v]:
                if not visited[neighbour]:
                    que.append(neighbour)
                    visited[neighbour] = True


if __name__ == "__main__":
    g = Graph()
    
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    
    print(g.adj_list)
    g.bfs(0)