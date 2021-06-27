"""
785. Is Graph Bipartite?
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where grapth[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:
- There are no self-edges (graph[u] does not contain u).
- There are no parallel edges (graph[u] does not contain duplicate values).
- If v is in graph[u], then u is in graph[v] (the graph is undirected)/
- The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B

Example1:
Input: n = 5, and edges = [[0, 1], [1, 2], [3, 4]]
Output: 2
"""

"""
Note:
1. BFS: O(V+E) time | O(V) space
"""




import unittest
import collections
from typing import List
class Solution(object):
    def isBipartite(self, graph: List[List[int]]) -> bool:  # dfs
        visited = [0] * len(graph)  # 0: unvisited, 1: yellow, -1: green
        for i in range(len(graph)):
            # unvisited node has edges
            if visited[i] == 0 and len(graph[i]) != 0:
                visited[i] = 1  # starting color
                queue = collections.deque([i])
                while len(queue) != 0:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if visited[neighbor] == 0:
                            visited[neighbor] = -visited[curr]
                            queue.append(neighbor)
                        elif visited[neighbor] == visited[curr]:  # same color
                            return False
        return True


# Unit Tests
funcs = [Solution().isBipartite]


class TestIsBipartite(unittest.TestCase):
    def testIsBipartite1(self):
        for func in funcs:
            graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
            self.assertEqual(
                func(graph=graph), False)


if __name__ == "__main__":
    unittest.main()
