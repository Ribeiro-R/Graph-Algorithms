# pylint: disable=invalid-name
"""
Breadth First Search - Level order traversal
* Start from source *
* Traversal nodes in current level *
* Move to next leval *

BFS - Pseudo Code

BFS(s) ->
    add s in the queue
    mark s as visited # Remove from queue
    while queue is not empty ->
        current = first element of queue
            if current has adjacent unvisited vertices ->
                add adj to queue
                mark adj as visited

        print(current)
"""

from typing import List


class BFS:
    """Breadth first search Class"""

    def __init__(self, vertices: int) -> None:
        self.v = vertices
        self.graph: List = [
            [] for i in range(self.v)
        ]  # Adjacent list representation

    def add_edge(self, src: int, dest: int) -> None:
        """Add edge to graph

        Args:
            src (int): source
            dest (int): destination
        """
        self.graph[src].append(dest)

    def bfs_traversal(self, s: int) -> None:
        """Apply bfs

        Args:
            s (int): source
        """
        visited = [False for i in range(self.v)]

        queue = [s]
        visited[s] = True

        while queue:
            curr = queue.pop(0)
            print(curr, end=" ")

            for adj in self.graph[curr]:
                if not visited[adj]:
                    queue.append(adj)
                    visited[adj] = True


if __name__ == "__main__":

    graph = BFS(12)

    graph.add_edge(1, 2)
    graph.add_edge(2, 6)
    graph.add_edge(6, 8)
    graph.add_edge(1, 3)
    graph.add_edge(8, 10)
    graph.add_edge(1, 4)
    graph.add_edge(3, 7)
    graph.add_edge(2, 5)
    graph.add_edge(6, 9)
    graph.add_edge(3, 6)
    graph.add_edge(8, 11)
    graph.add_edge(5, 8)
    graph.add_edge(7, 9)

    print("BFS Traversal")
    graph.bfs_traversal(1)
