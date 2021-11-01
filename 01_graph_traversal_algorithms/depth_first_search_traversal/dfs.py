# pylint: disable=invalid-name
"""
DFS - Recursive pseudo Code

DFS(S) ->
    mark s as visided
    if s is visited ->
        print(s)
    while s has adjacent nodes ->
        k - next node
            if (k is not visited) ->
                DFS(k)

DFS - Itarative pseudo Code

DFS(s) ->
    push s to "stack"

    while "stack" is not empty ->
        s = "stack".pop()
        if s is not visited ->
            set visited s (true)
            print(s)

    while s has adjacent elements ->
        k = next element
        if k is not visited ->
            "stack".push(k)

"""
from typing import List


class DFS:
    """Depth first search Class"""

    def __init__(self, vertices: int) -> None:
        self.v = vertices
        self.graph: List = [
            [] for i in range(self.v)
        ]  # Adjacent list representation
        self.visited = [False for i in range(self.v)]

    def add_edge(self, src: int, dest: int) -> None:
        """Add edge to graph

        Args:
            src (int): source
            dest (int): destination
        """
        self.graph[src].append(dest)

    def dfs_recursive(self, v: int):
        """Apply recursive DFS

        Args:
            v (int): vertices
        """
        self.visited[v] = True
        print(v, end=" ")

        # Recursively for all adjacent vertices
        for adj in self.graph[v]:
            if not self.visited[adj]:
                self.dfs_recursive(adj)

    def dfs_iterative(self, s: int):
        """Apply iterate DFS

        Args:
            s (int): source / node
        """
        self.visited = [False for i in range(self.v)]

        stack = [s]
        while len(stack) != 0:
            s = stack.pop()

            if not self.visited[s]:
                print(s, end=" ")
                self.visited[s] = True

            for v in self.graph[s]:
                if not self.visited[v]:
                    stack.append(v)


if __name__ == "__main__":

    graph = DFS(13)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 5)
    graph.add_edge(2, 4)
    graph.add_edge(2, 10)
    graph.add_edge(2, 5)
    graph.add_edge(2, 7)
    graph.add_edge(3, 6)
    graph.add_edge(4, 7)
    graph.add_edge(5, 2)
    graph.add_edge(5, 8)
    graph.add_edge(6, 9)
    graph.add_edge(8, 11)
    graph.add_edge(11, 12)

    print("DFS Recursive")
    graph.dfs_recursive(1)
    print("")
    print("DFS Iterative")
    graph.dfs_iterative(1)
