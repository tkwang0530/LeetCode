
"""
2368. Reachable Nodes With Restrictions
description: https://leetcode.com/problems/reachable-nodes-with-restrictions/description/
"""

"""
Note:
1. BFS+HashSet: O(V+E) time | O(V+E) space - where E is the number of edges in tree and V is the number of vertices in tree
"""

from typing import List
import collections
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = collections.deque([0])
        visited = set([0])
        restrictSet = set(restricted)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visited or neighbor in restrictSet:
                    continue

                visited.add(neighbor)
                queue.append(neighbor)
        return len(visited)

# Unit Tests
import unittest
funcs = [Solution().reachableNodes]

class TestReachableNodes(unittest.TestCase):
    def testReachableNodes1(self):
        for reachableNodes in funcs:
            n = 7
            edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
            restricted = [4,5]
            self.assertEqual(reachableNodes(n=n, edges=edges, restricted=restricted), 4)


    def testReachableNodes2(self):
        for reachableNodes in funcs:
            n = 7
            edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
            restricted = [4,2,1]
            self.assertEqual(reachableNodes(n=n, edges=edges, restricted=restricted), 3)

if __name__ == "__main__":
    unittest.main()