class Graph:
    """
    An undirected weighted graph implemented using an adjacency matrix.
    
    Attributes:
        vertices_count (int): The number of vertices in the graph.
        adj_matrix (list[list[int]]): The adjacency matrix representation of the graph.
        vertices_map (dict[str, int]): Mapping of vertex names to their indices.
        reverse_map (dict[int, str]): Mapping of indices to vertex names.
    """
    
    def __init__(self, vertices: list[str]) -> None:
        """
        Initialize the graph with a list of vertex names.
        Args:
            vertices: A list of unique vertex names.
        """
        if not vertices:
            raise ValueError("Vertices list cannot be empty")
            
        # Check for duplicate vertices
        if len(vertices) != len(set(vertices)):
            raise ValueError("All vertex names must be unique")
            
        self.vertices_count: int = len(vertices)
        self.adj_matrix: list[list[int]] = [[0] * self.vertices_count for _ in range(self.vertices_count)]
        self.vertices_map: dict[str, int] = self._create_vertices_map(vertices)
        self.reverse_map: dict[int, str] = {index: vertex for vertex, index in self.vertices_map.items()}
    

    def _create_vertices_map(self, vertices: list[str]) -> dict[str, int]:
        """
        Convert a list of vertices into a dictionary mapping vertex names to indices.
        Args:
            vertices: A list of vertex names.
        Returns:
            A dictionary mapping vertex names to their indices.
        """
        return {vertex: index for index, vertex in enumerate(vertices)}
    

    def _validate_vertex(self, vertex: str) -> None:
        """
        Validate that a vertex exists in the graph.
        Args:
            vertex: The vertex name to validate.  
        Raises:
            KeyError: If the vertex does not exist in the graph.
        """
        if vertex not in self.vertices_map:
            raise KeyError(f"Vertex '{vertex}' does not exist in the graph")
    

    def add_edge(self, vertex_i: str, vertex_j: str, weight: int = 1) -> None:
        """
        Add an edge between two vertices with an optional weight.  
        Args:
            vertex_i: The first vertex.
            vertex_j: The second vertex.
            weight: The weight of the edge (default: 1).
        Raises:
            KeyError: If either vertex does not exist in the graph.
            ValueError: If weight is negative.
        """
        # Validate vertices
        self._validate_vertex(vertex_i)
        self._validate_vertex(vertex_j)
        
        # Validate weight
        if weight < 0:
            raise ValueError("Edge weight cannot be negative")
            
        # Get indices
        index_i = self.vertices_map[vertex_i]
        index_j = self.vertices_map[vertex_j]
        
        # Add edge (undirected)
        self.adj_matrix[index_i][index_j] = weight
        self.adj_matrix[index_j][index_i] = weight
    

    def remove_edge(self, vertex_i: str, vertex_j: str) -> None:
        """
        Remove an edge between two vertices.
        Args:
            vertex_i: The first vertex.
            vertex_j: The second vertex.
        Raises:
            KeyError: If either vertex does not exist in the graph.
        """
        # Validate vertices
        self._validate_vertex(vertex_i)
        self._validate_vertex(vertex_j)
        
        # Get indices
        index_i = self.vertices_map[vertex_i]
        index_j = self.vertices_map[vertex_j]
        
        # Remove edge
        self.adj_matrix[index_i][index_j] = 0
        self.adj_matrix[index_j][index_i] = 0
    
    def has_edge(self, vertex_i: str, vertex_j: str) -> bool:
        """
        Check if an edge exists between two vertices.
        Args:
            vertex_i: The first vertex.
            vertex_j: The second vertex. 
        Returns:
            True if an edge exists, False otherwise.
        Raises:
            KeyError: If either vertex does not exist in the graph.
        """
        # Validate vertices
        self._validate_vertex(vertex_i)
        self._validate_vertex(vertex_j)
        
        # Get indices
        index_i = self.vertices_map[vertex_i]
        index_j = self.vertices_map[vertex_j]
        
        # Check if edge exists
        return self.adj_matrix[index_i][index_j] > 0
    

    def get_edge_weight(self, vertex_i: str, vertex_j: str) -> int:
        """
        Get the weight of an edge between two vertices.
        Args:
            vertex_i: The first vertex.
            vertex_j: The second vertex.
        Returns:
            The weight of the edge.  
        Raises:
            KeyError: If either vertex does not exist in the graph.
        """
        # Validate vertices
        self._validate_vertex(vertex_i)
        self._validate_vertex(vertex_j)
        
        # Get indices
        index_i = self.vertices_map[vertex_i]
        index_j = self.vertices_map[vertex_j]
        
        # Return edge weight
        return self.adj_matrix[index_i][index_j]
    

    def get_neighbors(self, vertex: str) -> list[str]:
        """
        Get all neighbors of a vertex.
        Args:
            vertex: The vertex to get neighbors for.  
        Returns:
            A list of neighboring vertices.
        Raises:
            KeyError: If the vertex does not exist in the graph.
        """
        # Validate vertex
        self._validate_vertex(vertex)
        
        # Get index
        index = self.vertices_map[vertex]
        
        # Find neighbors
        neighbors = []
        for neighbor_index, weight in enumerate(self.adj_matrix[index]):
            if weight > 0:
                neighbors.append(self.reverse_map[neighbor_index])
                
        return neighbors
    
    def print_graph(self) -> None:
        """Print the graph in an adjacency list format."""
        for row_index in range(self.vertices_count):
            vertex = self.reverse_map[row_index]
            print(f"{vertex}: ", end="")
            neighbors = []
            for col_index in range(self.vertices_count):
                weight = self.adj_matrix[row_index][col_index]
                if weight > 0:
                    neighbor_vertex = self.reverse_map[col_index]
                    if weight == 1:
                        neighbors.append(neighbor_vertex)
                    else:
                        neighbors.append(f"{neighbor_vertex}({weight})")
            print(" ".join(neighbors))
    
    def __str__(self) -> str:
        """
        String representation of the graph.
        
        Returns:
            A string representation of the graph.
        """
        result = []
        for row_index in range(self.vertices_count):
            vertex = self.reverse_map[row_index]
            neighbors = []
            for col_index in range(self.vertices_count):
                weight = self.adj_matrix[row_index][col_index]
                if weight > 0:
                    neighbor_vertex = self.reverse_map[col_index]
                    if weight == 1:
                        neighbors.append(neighbor_vertex)
                    else:
                        neighbors.append(f"{neighbor_vertex}({weight})")
            result.append(f"{vertex}: {' '.join(neighbors)}")
        return "\n".join(result)
    
    def __repr__(self) -> str:
        """
        Detailed string representation of the graph.
        Returns:
            A detailed string representation of the graph.
        """
        vertices = list(self.vertices_map.keys())
        return f"Graph(vertices={vertices})"


if __name__ == "__main__":
    nodes = ["A", "B", "C", "D"]
    g = Graph(nodes)

    g.add_edge("A", "B", 3)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 1)
    g.add_edge("C", "D", 4)

    print("Graph representation:")
    g.print_graph()
    
    print("\nString representation:")
    print(str(g))
    
    print("\nNeighbors of vertex 'A':", g.get_neighbors("A"))
    print("Edge weight between A and B:", g.get_edge_weight("A", "B"))
    print("Has edge between A and D:", g.has_edge("A", "D"))