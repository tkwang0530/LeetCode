"""
863. All Nodes Distance K in Binary Tree
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example1:
                3                                       
            /       \                            
         5           1                
      /     \        /    \
    6       2    0       8
           /    \                         
         7       4                         
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example2:
Input: root = [1], target = 1, k = 3
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 500]
0 <= Node.val <= 500
All the values Node.val are unique
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""

"""
Note:
1. Change to Graph and expand from target: O(n) time | O(n) space
(1) use hashTable to store graph info 3:[5, 1], 5:[3, 6, 2], 6:[5], etc ...
(2) use BFS starting from the target and keep tracking the level (using set visited, queue)
"""


from typing import List, Dict
from collections import defaultdict, deque
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        self.buildGraph(root, None, graph)
        result = []
        visited = set()
        queue = deque([(target, 0)])
        while len(queue) > 0:
            node, level = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if level == k:
                result.append(node.val)
            else:
                for connected in graph[node]:
                    queue.append((connected, level + 1))
        return result

    def buildGraph(self, node: TreeNode, parent: TreeNode, graph: Dict[TreeNode, List[TreeNode]]):
        if not node:
            return
        if parent:
            graph[node].append(parent)
        if node.left:
            graph[node].append(node.left)
            self.buildGraph(node.left, node, graph)
        if node.right:
            graph[node].append(node.right)
            self.buildGraph(node.right, node, graph)
        


# Unit Tests
funcs = [Solution().distanceK]


class TestDistanceK(unittest.TestCase):
    def testDistanceK1(self):
        for func in funcs:
            target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
            root = TreeNode(3, target, TreeNode(1, TreeNode(0), TreeNode(8)))
            k = 2
            self.assertEqual(sorted(func(root=root, target=target, k=k)), sorted([7, 4, 1]))

    def testDistanceK2(self):
        for func in funcs:
            target = root = TreeNode(1)
            k = 3
            self.assertEqual(sorted(func(root=root, target=target, k=k)), sorted([]))


if __name__ == "__main__":
    unittest.main()
