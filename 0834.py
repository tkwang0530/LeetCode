"""
834. Sum of Distances in Tree
description: https://leetcode.com/problems/sum-of-distances-in-tree/description/
"""

"""
Note:
1. PostOrder dfs + PreOrder dfs: O(n) time | O(n) space - where n is the number of nodes
res[2] = res[0] - count[2] + (n - count[2])
ref: https://www.youtube.com/watch?v=uRKhiznlaxg
"""

import unittest, collections
from typing import List
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [0] * n
        res = [0] * n

        def dfs(root, prev):
            for neighbor in graph[root]:
                if neighbor == prev:
                    continue
                dfs(neighbor, root)
                res[root] += res[neighbor] + count[neighbor]
                count[root] += count[neighbor]
            count[root] += 1
        def dfs2(root, prev):
            for neighbor in graph[root]:
                if neighbor == prev:
                    continue
                res[neighbor] = res[root] - count[neighbor] + n - count[neighbor]
                dfs2(neighbor, root)
        
        dfs(0, -1)
        dfs2(0, -1)
        return res

# Unit Tests
import unittest
funcs = [Solution().sumOfDistancesInTree]
class TestSumOfDistancesInTree(unittest.TestCase):
    def testSumOfDistancesInTree1(self):
        for func in funcs:
            n = 6
            edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
            self.assertEqual(func(n=n, edges=edges), [8,12,6,10,10,10])

    def testSumOfDistancesInTree2(self):
        for func in funcs:
            n = 1
            edges = []
            self.assertEqual(func(n=n, edges=edges), [0])

    def testSumOfDistancesInTree3(self):
        for func in funcs:
            n = 2
            edges = [[1,0]]
            self.assertEqual(func(n=n, edges=edges), [1,1])

if __name__ == "__main__":
    unittest.main()
