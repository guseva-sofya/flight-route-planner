from typing import List

# type alias to use for vertices instead of raw ints
Vertex = int


class Graph:
    """Graph represents a bidirectional weighted graph.

    Attributes:
        _adjacency_matrix: A matrix of integers with a size of
        [num_vertices x num_vertices]
        filled with the edge weights between vertices.
        Initially filled with "-1" indicating no relationship between vertices.
    """

    _adjacency_matrix: List[List[int]]

    def __init__(self, num_vertices: int):
        """Initializes the instance based on the number of vertices defined by user.

        Args:
            num_vertices: An integer that represents number of vertices in a graph.
        """

        self._adjacency_matrix = [
            [-1 for _ in range(num_vertices)] for _ in range(num_vertices)
        ]

    def num_vertices(self) -> int:
        return len(self._adjacency_matrix)

    def vertices(self) -> List[Vertex]:
        return list(range(self.num_vertices()))

    def add_edge(self, vertex1: Vertex, vertex2: Vertex, weight: int) -> None:
        """Adds edge weights into adjacency matrix.

        Args:
            vertex1, vertex2: Two integers that represent two vertices
            between which we need to add the edge weight.
            weight: An integer represent the edge weight.

        Raises:
            ValueError: An error raised if edge weights or weight are negative
            or one of the vertices value is more than the size
            of the adjacency matrix.
        """

        if vertex1 < 0 or vertex1 >= self.num_vertices():
            raise ValueError(f"Invalid first vertex index: {vertex1}")
        if vertex2 < 0 or vertex2 >= self.num_vertices():
            raise ValueError(f"Invalid second vertex index: {vertex2}")
        if weight < 0:
            raise ValueError(f"Negative weights are not allowed: {weight}")

        self._adjacency_matrix[vertex1][vertex2] = weight
        self._adjacency_matrix[vertex2][vertex1] = weight

    def edge_weight(self, vertex1: Vertex, vertex2: Vertex) -> int:
        weight = self._adjacency_matrix[vertex1][vertex2]
        return weight

    def find_neighbors(self, vertex: Vertex) -> List[Vertex]:
        matrix_row = self._adjacency_matrix[vertex]
        neighbors = [index for index, value in enumerate(matrix_row) if value != -1]
        return neighbors
