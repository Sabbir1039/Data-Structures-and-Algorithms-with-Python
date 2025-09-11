from collections import deque

def bfs(graph: dict[str, list[str]], start_vertex: str) -> list[str]:
    queue = deque()
    seen = set()
    results = []
    queue.append(start_vertex)
    seen.add(start_vertex)

    while queue:
        vertex = queue.popleft()
        results.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in seen:
                queue.append(neighbour)
                seen.add(neighbour)
    return results


def dfs(graph: dict[str, list[str]], start_vertex: str) -> list[str]:
    stack = deque()
    seen = set()
    results = []
    stack.append(start_vertex)
    seen.add(start_vertex)

    while stack:
        curr_vertex = stack.pop()
        results.append(curr_vertex)

        for neighbour in graph[curr_vertex]:
            if neighbour not in seen:
                stack.append(neighbour)
                seen.add(neighbour)
    return results

def dfs_recursive(
        graph: dict[str, list[str]],
        vertex: str,
        seen: set[str] = None,
        results: list[str] = None
        ) -> list[str]:
    if seen is None:
        seen = set()
    if results is None:
        results = []
    
    results.append(vertex)
    seen.add(vertex)

    for neighbour in graph[vertex]:
        if neighbour not in seen:
            dfs_recursive(graph, neighbour, seen, results)
    return results



if __name__ == "__main__":
    graph = {
        "A": ["C", "B"],
        "B": [],
        "C": ["D", "E"],
        "D": [],
        "E": []
    }
    bfs_list = bfs(graph, "A")
    print(bfs_list)

    dfs_list = dfs(graph, "A")
    print(dfs_list)

    dfs_list = dfs_recursive(graph, "A")
    print(dfs_list)