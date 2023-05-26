"""
1245. Tree Diameter
The diameter of a tree is the number of edges in the longest path in that tree.

There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.

Return the diameter of the tree.

Example1:
Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: The longest path of the tree is the path 1 - 0 - 2.

Example2:
Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.

Constraints:
n == edges.length + 1
1 <= n <= 10^4
0 <= a_i, b_i < n
a_i != b_i
"""

"""
Note:
1. dfs+minHeap: O(V+Elog(2)) time | O(V+E) space - where V is the number of nodes of the tree and E is the number of edges 
"""

import unittest
import heapq, collections
from typing import List, Tuple
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
    
        graph = collections.defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        def dfs(node, parent) -> Tuple[int]: # level, diameter
            minHeapLevel = []
            maxDiameter = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                neighborLevel, neighborDiameter = dfs(neighbor, node)
                maxDiameter = max(maxDiameter, neighborDiameter)
                if len(minHeapLevel) < 2:
                    heapq.heappush(minHeapLevel, neighborLevel)
                else:
                    heapq.heappushpop(minHeapLevel, neighborLevel)

            includeRootDiameter = sum(minHeapLevel)
            excludeRootDiameter = maxDiameter
            level = minHeapLevel[-1]+1 if minHeapLevel else 1
            diameter = max(includeRootDiameter, excludeRootDiameter)

            return level, diameter
        
        return dfs(edges[0][0], -1)[1]

# Unit Tests
import unittest
funcs = [Solution().treeDiameter]
class TestTreeDiameter(unittest.TestCase):
    def testTreeDiameter1(self):
        for func in funcs:
            edges = [[0,1],[0,2]]
            self.assertEqual(func(edges=edges), 2)

    def testTreeDiameter2(self):
        for func in funcs:
            edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
            self.assertEqual(func(edges=edges), 4)

if __name__ == "__main__":
    unittest.main()
