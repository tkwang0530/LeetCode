"""
2096. Step-By-Step Directions From a Binary Tree Node to Another
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t.
Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
- 'L' means to go from a node to its left child node.
- 'R' means to go from a node to its right child node.
- 'U' means to go from a node to its parent node.

Return the step-by-step directions of the shortest path from node s to node t.

Example1:
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

Example2:
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

Constraints:
The number of nodes in the tree is n.
2 <= n <= 10^5
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
"""

""" 
1. DFS (Preorder-Record-Directions): O(n) time | O(h) space
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startDirections = []
        endDirections = []
        def dfs(node, directions):
            nonlocal startDirections, endDirections
            if not node:
                return
            if node.val == startValue:
                startDirections = directions.copy()

            if node.val == destValue:
                endDirections = directions.copy()

            if node.left:
                directions.append("L")
                dfs(node.left, directions)
                directions.pop()

            if node.right:
                directions.append("R")
                dfs(node.right, directions)
                directions.pop()
        
        directions = []
        dfs(root, directions)

        n, m = len(startDirections), len(endDirections)
        for i in range(min(n, m)):
            startD, endD = startDirections[i], endDirections[i]
            if startD != endD:
                return (n-i) * "U" + "".join(endDirections[i:])

        return (n-min(n, m)) * "U" + "".join(endDirections[min(n, m):])

# Unit Tests
import unittest
funcs = [Solution().getDirections]


class TestGetDirections(unittest.TestCase):
    def testGetDirections1(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4)))
            startValue = 3
            destValue = 6
            self.assertEqual(func(root=root, startValue=startValue, destValue=destValue), "UURL")

    def testGetDirections2(self):
        for func in funcs:
            root = TreeNode(2, TreeNode(1))
            startValue = 2
            destValue = 1
            self.assertEqual(func(root=root, startValue=startValue, destValue=destValue), "L")

if __name__ == "__main__":
    unittest.main()
