"""
1743. Restore the Array From Adjacent Pairs
description: https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/
"""

"""
Note:
1. BFS + HashSet: O(2n) time | O(2n) space - where n is the length of adjacentPairs // 2
"""

from typing import List
import unittest, collections
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        startNode = -float("inf")
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                startNode = node
                break

        visited = set()
        queue = collections.deque([startNode])
        visited.add(startNode)
        output = []
        while queue:
            node = queue.popleft()
            output.append(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return output

# Unit Tests
funcs = [Solution().restoreArray]


class TestRestoreArray(unittest.TestCase):
    def testRestoreArray1(self):
        for func in funcs:
            adjacentPairs = [[2,1],[3,4],[3,2]]
            self.assertEqual(func(adjacentPairs=adjacentPairs), [1,2,3,4])

    def testRestoreArray2(self):
        for func in funcs:
            adjacentPairs = [[4,-2],[1,4],[-3,1]]
            self.assertEqual(func(adjacentPairs=adjacentPairs), [-2,4,1,-3])

    def testRestoreArray3(self):
        for func in funcs:
            adjacentPairs = [[100000,-100000]]
            self.assertEqual(func(adjacentPairs=adjacentPairs), [100000,-100000])


if __name__ == "__main__":
    unittest.main()
