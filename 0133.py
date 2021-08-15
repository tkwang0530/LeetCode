"""
133. Clone Graph
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Example4:
Input: adjList = [[2],[1]]
Output: [[2],[1]]


Constraints:
The number of nodes in the graph is in the range [0, 100]
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""

"""
Note:
1. Iterative BFS: O(V+E) time | O(V+E) space
2. Iterative DFS: O(V+E) time | O(V+E) space
3. Recursive DFS: O(V+E) time | O(V+E) space
"""


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Dict, List
import unittest
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        nodeCopy = Node(node.val)
        dict = {node: nodeCopy}
        queue = deque([node])
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dict: # neighbor is not visited
                    neighborCopy = Node(neighbor.val)
                    dict[neighbor] = neighborCopy
                    dict[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dict[node].neighbors.append(dict[neighbor])
        return nodeCopy

    def cloneGraph2(self, node: Node) -> Node:
        if not node:
            return node
        nodeCopy = Node(node.val)
        dict = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dict:
                    neighborCopy = Node(neighbor.val)
                    dict[neighbor] = neighborCopy
                    dict[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dict[node].neighbors.append(dict[neighbor])
        return nodeCopy

    def cloneGraph3(self, node: Node) -> Node:
        if not node:
            return node
        nodeCopy = Node(node.val)
        dict = { node: nodeCopy }
        self.dfs(node, dict)
        return nodeCopy
    
    def dfs(self, node: Node, dict: Dict[Node, List[Node]]) -> None:
        for neighbor in node.neighbors:
            if neighbor not in dict:
                neighborCopy = Node(neighborCopy)
                dict[neighbor] = neighborCopy
                dict[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dict)
            else:
                dict[node].neighbors.append(dict[neighbor])



# Unit Tests
funcs = [Solution().cloneGraph, Solution().cloneGraph2]


class TestCloneGraph(unittest.TestCase):
    def testCloneGraph1(self):
        for func in funcs:
            node1 = Node(1)
            node2 = Node(2)
            node3 = Node(3)
            node4 = Node(4)
            node1.neighbors = [node2, node4]
            node2.neighbors = [node1, node3]
            node3.neighbors = [node2, node4]
            node4.neighbors = [node1, node3]
            nodeCopy = func(node1)
            self.assertEqual(nodeCopy == node1, False)
            self.assertEqual(nodeCopy.val, 1)
            self.assertEqual((sorted([neighbor.val for neighbor in nodeCopy.neighbors])), sorted([2, 4]))
            self.assertEqual((sorted([neighbor.val for neighbor in nodeCopy.neighbors[0].neighbors])), sorted([1, 3]))
            self.assertEqual((sorted([neighbor.val for neighbor in nodeCopy.neighbors[1].neighbors])), sorted([1, 3]))

    def testCloneGraph2(self):
        for func in funcs:
            node1 = Node(1)
            node1.neighbors = []
            nodeCopy = func(node1)
            self.assertEqual(nodeCopy == node1, False)
            self.assertEqual(nodeCopy.val, 1)
            self.assertEqual((sorted([neighbor.val for neighbor in nodeCopy.neighbors])), sorted([]))

    def testCloneGraph3(self):
        for func in funcs:
            node1 = None
            nodeCopy = func(node1)
            self.assertEqual(nodeCopy, None)

    def testCloneGraph4(self):
        for func in funcs:
            node1 = Node(1)
            node2 = Node(2)
            node1.neighbors = [node2]
            node2.neighbors = [node1]
            nodeCopy = func(node1)
            self.assertEqual(nodeCopy == node1, False)
            self.assertEqual(nodeCopy.val, 1)
            self.assertEqual((sorted([neighbor.val for neighbor in nodeCopy.neighbors])), sorted([2]))
            self.assertEqual((sorted([neighbor.val for neighbor in nodeCopy.neighbors[0].neighbors])), sorted([1]))


if __name__ == "__main__":
    unittest.main()
