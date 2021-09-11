"""
104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example1:
Given binary tree [3, 9, 20, null, null, 15, 7]
        3
      /    \
    9     20
           /   \
        15    7
return its depth = 3.
"""

"""
Note:
1. Recursion (stop at None): O(n) time | O(n) space
2. Recursion (stop at leaf): O(n) time | O(n) space
3. Iteration (DFS - PreOrder Traversal): O(n) time | O(n) space
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth3(self, root: TreeNode) -> int:
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
funcs = [Solution().maxDepth, Solution().maxDepth2, Solution().maxDepth3]

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
