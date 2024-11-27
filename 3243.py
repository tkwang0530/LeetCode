"""
3243. Shortest Distance After Road Addition Queries I
description: https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/
"""

"""
Note:
1. BFS (Layer order traversal): O(q*(n+q)^2) time | O(n+q) space - where q is the length of array queries 
"""

from typing import List
import collections
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u in range(n-1):
            graph[u].append(u+1)
        
        
        def bfs():
            current = [0] # city
            steps = 0
            visited = set()
            while current:
                nextCities = []
                for u in current:
                    if u == n-1:
                        return steps
                    
                    for v in graph[u]:
                        if v in visited:
                            continue
                        visited.add(v)
                        nextCities.append(v)
                steps += 1
                current = nextCities
            return steps

        output = []
        for u, v in queries:
            graph[u].append(v)
            output.append(bfs())

        return output

import unittest
funcs = [Solution().shortestDistanceAfterQueries]

class TestShortestDistanceAfterQueries(unittest.TestCase):
    def testShortestDistanceAfterQueries1(self):
        for func in funcs:
            n = 5
            queries = [[2,4],[0,2],[0,4]]
            self.assertEqual(func(n=n, queries=queries), [3,2,1])

    def testShortestDistanceAfterQueries2(self):
        for func in funcs:
            n = 4
            queries = [[0,3],[0,2]]
            self.assertEqual(func(n=n, queries=queries), [1,1]) 

if __name__ == "__main__":
    unittest.main()
