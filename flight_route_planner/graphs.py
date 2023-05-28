from typing import List


class Graph:
    """
    Graph represents a bidirectional weighted graph. Edge weights should be
    non-negative.
    """

    _adjacency_matrix: List[List[int]]

    # adjacency_matrix creation
    def __init__(self, num_vertices: int):
        self._adjacency_matrix = [
            [-1 for _ in range(num_vertices)] for _ in range(num_vertices)
        ]

    def size(self) -> int:
        return len(self._adjacency_matrix)

    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        if vertex1 < 0 or vertex1 >= self.size():
            raise ValueError(f"Invalid first vertex index: {vertex1}")
        if vertex2 < 0 or vertex2 >= self.size():
            raise ValueError(f"Invalid second vertex index: {vertex2}")
        if weight < 0:
            raise ValueError(f"Negative weights are not allowed: {weight}")

        self._adjacency_matrix[vertex1][vertex2] = weight
        self._adjacency_matrix[vertex2][vertex1] = weight

    def find_neighbors(self, vertex: int) -> List[int]:
        matrix_row = self._adjacency_matrix[vertex]
        neighbors = [index for index, value in enumerate(matrix_row) if value != -1]
        return neighbors
