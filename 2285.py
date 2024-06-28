"""
2285. Maximum Total Importance of Roads
description: https://leetcode.com/problems/maximum-total-importance-of-roads/description/
"""

"""
Note:
1. Greedy: O(nlogn) time | O(n+r) space - where r is the number of roads
"""


import unittest, collections
from typing import List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        cities = sorted([city for city in range(n)], key = lambda x: -len(graph[x]))
        maxSum = 0
        value = n
        for city in cities:
            maxSum += value * len(graph[city])
            value -= 1
        return maxSum
    
# Unit Tests
funcs = [Solution().maximumImportance]


class TestMaximumImportance(unittest.TestCase):
    def testMaximumImportance1(self):
        for maximumImportance in funcs:
            n = 5
            roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
            self.assertEqual(maximumImportance(n, roads), 43)

    def testMaximumImportance2(self):
        for maximumImportance in funcs:
            n = 5
            roads = [[0,3],[2,4],[1,3]]
            self.assertEqual(maximumImportance(n, roads), 20)

if __name__ == "__main__":
    unittest.main()
