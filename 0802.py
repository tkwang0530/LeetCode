"""
802. Find Eventual Safe States
description: https://leetcode.com/problems/find-eventual-safe-states/description/
"""

"""
Note:
1. backtrack: O(m+n) time | O(n) space - where m is the number of nodes and m is the number of edges
"""

from typing import List
import unittest

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visiting = set()
        memo = {}
        def isSafeNode(node: int) -> bool:
            if not graph[node]:
                return True

            if node in memo:
                return memo[node]
            if node in visiting:
                memo[node] = False
            else:
                visiting.add(node)
                isSafe = True
                for child in graph[node]:
                    isSafe = isSafe and isSafeNode(child)
                visiting.remove(node)
                memo[node] = isSafe
            return memo[node]
        
        output = []
        for node in range(len(graph)):
            if isSafeNode(node):
                output.append(node)
        return output

# Unit Tests
funcs = [Solution().eventualSafeNodes]


class TestEventualSafeNodes(unittest.TestCase):
    def testEventualSafeNodes1(self):
        for func in funcs:
            graph = [[1,2],[2,3],[5],[0],[5],[],[]]
            self.assertEqual(func(graph=graph), [2,4,5,6])

    def testEventualSafeNodes2(self):
        for func in funcs:
            graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
            self.assertEqual(func(graph=graph), [4])

if __name__ == "__main__":
    unittest.main()
