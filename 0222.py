"""
222. Count Complete Tree Nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2^h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example1:
                1
            /        \
          2           3
       /     \        /
     4       5     6
Input: root = [1,2,3,4,5,6]
Output: 6

Example2:
Input: root = []
Output: 0

Example3:
Input: root = [1]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 5 * 10^4]
0 <= Node.val <= 5 * 10^4
The tree is guaranteed to be complete.
"""

"""
Note:
1. Brute Force - DFS: O(n) time | O(logn) space
2. Recursion: O(logn * logn) time | O(logn) space
compare the depth between left subtree and right subtree
(1) if left subtree height equals right subtree height:
a. left subtree is perfect binary tree
b. right subtree is complete binary tree
(2) if left subtree height is greater than right subtree height:
a. left subtree is complete binary tree
b. right subtree is perfect binary tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        resultContainer = [0]
        self.dfs(root, resultContainer)
        return resultContainer[0]
        
    def dfs(self, root, resultContainer) -> None:
        resultContainer[0] += 1
        if root.left:
            self.dfs(root.left, resultContainer)
        if root.right:
            self.dfs(root.right, resultContainer)

    def countNodes2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return 2 ** leftDepth + self.countNodes(root.right)
        else:
            return 2 ** rightDepth + self.countNodes(root.left)
    
    def getDepth(self, root) -> int:
        if not root:
            return 0
        return 1 + self.getDepth(root.left)


# Unit Tests
import unittest
funcs = [Solution().countNodes, Solution().countNodes2]


class TestCountNodes(unittest.TestCase):
    def testCountNodes1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
            self.assertEqual(func(root=root), 6)

    def testCountNodes2(self):
        for func in funcs:
            root = None
            self.assertEqual(func(root=root), 0)

    def testCountNodes3(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), 1)


if __name__ == "__main__":
    unittest.main()
