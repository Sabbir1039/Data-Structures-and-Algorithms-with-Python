from collections import defaultdict, deque

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    # time complexity of DFS in an undirected graph is O(V+E)
    # DFS using recursion
    def dfs(self, source, visited=None):
        if visited is None:
            visited = []
        
        visited.append(source)
        print(source, end=" ")
        
        for neighbour in self.graph[source]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)
    
    # DFS using stack
    def dfs_stack(self, source):
        visited = set()
        stack = [source]
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                
                for neighbour in self.graph[vertex]:
                    if neighbour not in visited:
                        stack.append(neighbour)
    
if __name__ == "__main__":
    g = Graph()
    
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    
    g.dfs(0)
    print('\n')
    g.dfs_stack(0)
    
# Graph: 
#        0
#       / \
#      1   2
#     /     \
#    3       4
#             \
#              5
