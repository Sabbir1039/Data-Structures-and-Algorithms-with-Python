from collections import deque

class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_edge(self, u, v):
        self.graph[u] = self.graph.get(u, [])
        self.graph[u].append(v)
    
    def print_vertices(self):
        for key, value in self.graph.items():
            print(f"Vertices[{key}] : ", end="")
            
            for node in value:
                print(f" -> {node}", end="")
            print('\n')
    
    def bfs(self, start):
        q = deque()
        visited = []
        vertices = []
        
        q.append(start)
        visited.append(start)
        
        while q:
            node = q.popleft()
            vertices.append(node)
            
            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.append(neighbour)
        return vertices
    
    def dfs(self, start):
        stack = deque()
        visited = []
        data = []
        
        stack.append(start)
        visited.append(start)
        
        while stack:
            node = stack.pop()
            data.append(node)
            
            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.append(neighbour)
        return data
    
if __name__ == "__main__":
    graph = Graph()
    
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('D', 'A')
    
    graph.print_vertices()
    
    print(graph.bfs('A'))
    print(graph.dfs('A'))
