def has_path_undirected(src, dest, graph) -> bool:
    if src == dest:
        return True
    
    if src not in graph:
        return False
    
    ans = False
    for neighbour in graph[src]:
        ans = ans or has_path_undirected(neighbour, dest, graph)
    return ans

if __name__ == "__main__":
    graph = {
        0: [1],
        1: [2, 3],
        2: [4],
        3: [0],
        4: [],
    }
    
    print(has_path_undirected(2, 3, graph))