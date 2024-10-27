"""
104. Maximum Depth of Binary Tree
description: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

"""
Note:
1. DFS (PostOrder Traversal): O(n) time | O(h) space - where n is the number of nodes and h is the height of the tree
2. Iteration (DFS - PreOrder Traversal): O(n) time | O(n) space - where n is the number of nodes
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            maxDepth = 1
            if node.left:
                maxDepth = max(maxDepth, 1+dfs(node.left))
            if node.right:
                maxDepth = max(maxDepth, 1+dfs(node.right))

            return maxDepth

        return dfs(root)

class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        maxDep = 0
        while len(stack) > 0:
            node, level = stack.pop()
            maxDep = max(maxDep, level)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        return maxDep
# Unit Tests
import unittest
funcs = [Solution().maxDepth, Solution2().maxDepth]

class TestMaxDepth(unittest.TestCase):
    def testMaxDepth1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)))
            self.assertEqual(func(root=root), 3)

    def testMaxDepth2(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2))
            self.assertEqual(func(root=root), 2)

    def testMaxDepth3(self):
        for func in funcs:
            root = None
            self.assertEqual(func(root=root), 0)

    def testMaxDepth4(self):
        for func in funcs:
            root = TreeNode(0)
            self.assertEqual(func(root=root), 1)


if __name__ == "__main__":
    unittest.main()
