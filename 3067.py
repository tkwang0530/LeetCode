"""
3067. Count Pairs of Connectable Servers in a Weighted Tree Network
description: https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/description/
"""

"""
Note:
1. BFS+ HashTable: O(V^2 + VE) time | O(V+E) space
"""

from typing import List
import collections
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        output = [0] * n
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        for i in range(n):
            visited = set([i])
            queue = collections.deque([])
            validBranchNodeCounts = collections.defaultdict(int) # {branchNode: count}
            for (neighborNode, weight) in graph[i]:
                queue.append((neighborNode, weight, neighborNode))
                
            while queue:
                node, runningSum, branchNode = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if runningSum % signalSpeed == 0:
                    validBranchNodeCounts[branchNode] += 1
                
                for (nextNode,weight) in graph[node]:
                    if nextNode in visited:
                        continue
                    queue.append((nextNode, runningSum+weight, branchNode))
            
            totalValids = sum(validBranchNodeCounts.values())
            for node in validBranchNodeCounts.keys():
                output[i] += (totalValids - validBranchNodeCounts[node]) * validBranchNodeCounts[node]
            output[i] //= 2
        return output

# Unit Tests
import unittest
funcs = [Solution().countPairsOfConnectableServers]


class TestCountPairsOfConnectableServers(unittest.TestCase):
    def testCountPairsOfConnectableServers1(self):
        for func in funcs:
            edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]]
            signalSpeed = 1
            self.assertEqual(func(edges=edges, signalSpeed=signalSpeed), [0,4,6,6,4,0])

    def testCountPairsOfConnectableServers2(self):
        for func in funcs:
            edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]]
            signalSpeed = 3
            self.assertEqual(func(edges=edges, signalSpeed=signalSpeed), [2,0,0,0,0,0,2])

if __name__ == "__main__":
    unittest.main()
