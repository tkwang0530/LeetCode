"""
886. Possible Bipartition
description: https://leetcode.com/problems/possible-bipartition/description/
"""

"""
Note:
1. BFS+memo: O(n+d) time | O(n+d) space - where n is the number of people and d is the number of dislikes
color the nodes with 2 colors, and check if the adjacent nodes have the same color
"""

from typing import List
import collections
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = {}
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(node):
            if node in color:
                return True

            color[node] = True
            queue = collections.deque([node])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in color:
                        if color[node] == color[neighbor]:
                            return False
                        continue
                    color[neighbor] = not color[node]
                    queue.append(neighbor)
            return True

        for node in range(1, n+1):
            if bfs(node) == False:
                return False
        return True

# Unit Tests
import unittest
funcs = [Solution().possibleBipartition]

class TestPossibleBipartition(unittest.TestCase):
    def testPossibleBipartition1(self):
        for func in funcs:
            n = 4
            dislikes = [[1,2],[1,3],[2,4]]
            self.assertEqual(func(n=n, dislikes=dislikes), True)

    def testPossibleBipartition2(self):
        for func in funcs:
            n = 3
            dislikes = [[1,2],[1,3],[2,3]]
            self.assertEqual(func(n=n, dislikes=dislikes), False)

if __name__ == "__main__":
    unittest.main()
