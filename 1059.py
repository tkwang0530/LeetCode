"""
1059. All Paths from Source Lead to Destination
Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi, and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually, end at destination, that is:
- At least one path exists from the source node to the destination node
- If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
- The number of possible paths from source to destination is a finite number.

Return true if and only if all roads from source lead to destination.

Example1:
Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
Output: false
Explanation: It is possible to reach and get stuck on both node 1 and node 2.

Example2:
Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
Output: false
Explanation: We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.

Example3:
Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
Output: true

Constraints:
1 <= n <= 10^4
0 <= edges.length <= 10^4
edges[i].length == 2
0 <= ai, bi <= n - 1
0 <= source <= n - 1
0 <= destination <= n - 1
The given graph may have self-loops and parallel edges.
"""

"""
Note:
1. dfs + memo: O(V+E) time | O(V+E) space - where V is the number of nodes and E is the number of edges
"""

import collections
from typing import List
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        status = [0 for _ in range(n)] # 0: unknown, 1: visiting, 2: visited
        graph = collections.defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)

        if len(graph[destination]) > 0:
            return False

        status[source] = 2
        def dfs(node, status):
            if node == destination:
                return True

            if node != destination and not graph[node]:
                return False

            status[node] = 1
            allCanReach = True
            for child in graph[node]:
                if status[child] == 2:
                    continue
                if status[child] == 1:
                    allCanReach = False
                    break
                allCanReach = allCanReach and dfs(child, status)
            
            status[node] = 2
            return allCanReach

        return dfs(source, status)
# Unit Tests
import unittest
funcs = [Solution().leadsToDestination]

class TestLeadsToDestination(unittest.TestCase):
    def testLeadsToDestination1(self):
        for func in funcs:
            n = 3
            edges = [[0,1],[0,2]]
            source = 0
            destination = 2
            self.assertEqual(func(n=n, edges=edges, source=source, destination=destination), False)

    def testLeadsToDestination2(self):
        for func in funcs:
            n = 4
            edges = [[0,1],[0,3],[1,2],[2,1]]
            source = 0
            destination = 3
            self.assertEqual(func(n=n, edges=edges, source=source, destination=destination), False)

    def testLeadsToDestination3(self):
        for func in funcs:
            n = 4
            edges = [[0,1],[0,2],[1,3],[2,3]]
            source = 0
            destination = 3
            self.assertEqual(func(n=n, edges=edges, source=source, destination=destination), True)

if __name__ == "__main__":
    unittest.main()