inputs = [["A","B"], ["A", "C"], ["B", "D"], ["B", "E"], ["C", "F"], ["E", "F"]]
nodes = ["A", "B", "C", "D", "E", "F"]

node_index = {node: i for i, node in enumerate(nodes)}
adj_matrix = [[0 for _ in range(6)] for _ in range(6)]

print(node_index)

for edge in inputs:
    i = node_index[edge[0]]
    j = node_index[edge[1]]
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1 # Add this line for undirected graph

for row in adj_matrix:
    print(row)

# Output:
# {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
# [0, 1, 1, 0, 0, 0]
# [1, 0, 0, 1, 1, 0]
# [1, 0, 0, 0, 0, 1]
# [0, 1, 0, 0, 0, 0]
# [0, 1, 0, 0, 0, 1]
# [0, 0, 1, 0, 1, 0]

# Space Complexity: O(V**2)
# time Complexity: O(V**2 + E)

# Checking if an edge exists between two vertices: O(1)
# Adding an edge: O(1)
# Removing an edge: O(1)
# Iterating over all edges: O(V**2)
# Iterating over all neighbors of a vertex: O(V)