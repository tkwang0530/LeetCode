"""
1466. Reorder Routes to Make All Paths Lead to the City Zero
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, the ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [a_i, b_i] represents a road from city a_i to city b_i

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0.
Return the minimum number of edges changed.

It's guaranteed that each city reach city 0 after reorder.

Example1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0


Constraints:
2 <= n <= 5 * 10^4
connections.length == n - 1
connections[i].length == 2
0 <= a_i, b_i <= n - 1
a_i != b_i
"""

"""
Note:
1. Recursive DFS (using Set): O(n) time | O(n) space
(1) start at city 0
(2) recursively check its neighbors, to see if there is a link from neighbor to city
(3) count outgoing edges

2. Iterative BFS: O(n) time | O(n) space
"""

from collections import defaultdict, deque
from typing import List
import unittest
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # initialization
        edges = { (source, target) for source, target in connections }
        graph = defaultdict(list)
        visited = set()
        result = [0] # [changes]

        # build undirected graph
        for source, target in connections:
            graph[source].append(target)
            graph[target].append(source)

        # start to dfs on "city 0"
        visited.add(0)
        self.dfs(0, edges, graph, visited, result)
        return result[0]

    def dfs(self, city, edges, graph, visited, result) -> None:
        for neighbor in graph[city]:
            if neighbor in visited:
                continue
            # check if this neighbor can reach current city
            if (neighbor, city) not in edges:
                result[0] += 1
            visited.add(neighbor)
            self.dfs(neighbor, edges, graph, visited, result)

    def minReorder2(self, n: int, connections: List[List[int]]) -> int:
        edges = { (source, target) for source, target in connections}
        graph = defaultdict(list)
        for source, target in connections:
            graph[source].append(target)
            graph[target].append(source)
        
        queue = deque([0])
        visited = set([0])
        changes = 0
        while len(queue) > 0:
            city = queue.popleft()
            for neighbor in graph[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    changes += 1
                visited.add(neighbor)
                queue.append(neighbor)
        return changes

        
        






# Unit Tests
funcs = [Solution().minReorder, Solution().minReorder2]


class TestMinReorder(unittest.TestCase):
    def testMinReorder1(self):
        for func in funcs:
            n = 6
            connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
            self.assertEqual(func(n=n, connections=connections), 3)

    def testMinReorder2(self):
        for func in funcs:
            n = 5
            connections = [[1,0],[1,2],[3,2],[3,4]]
            self.assertEqual(func(n=n, connections=connections), 2)

    def testMinReorder3(self):
        for func in funcs:
            n = 3
            connections = [[1,0],[2,0]]
            self.assertEqual(func(n=n, connections=connections), 0)

if __name__ == "__main__":
    unittest.main()
