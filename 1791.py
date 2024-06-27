"""
1791. Find Center of Star Graph
description: https://leetcode.com/problems/find-center-of-star-graph/description/
"""

"""
Note:
1. hashSet: O(1) time | O(1) space
"""


import unittest
from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited = set()
        for u, v in edges[:2]:
            if u in visited:
                return u
            elif v in visited:
                return v
            
            visited.add(u)
            visited.add(v)
        return -1
    
# Unit Tests
funcs = [Solution().findCenter]


class TestFindCenter(unittest.TestCase):
    def testFindCenter1(self):
        for findCenter in funcs:
            self.assertEqual(findCenter(edges=[[1,2],[2,3],[4,2]]), 2)

    def testFindCenter2(self):
        for findCenter in funcs:
            edges = [[1,2],[5,1],[1,3],[1,4]]
            self.assertEqual(findCenter(edges), 1)

if __name__ == "__main__":
    unittest.main()
