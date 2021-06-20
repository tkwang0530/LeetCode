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
1. Using Base case 1 (stop at None): O(n) time | O(n) space
2. Using Base case 2 (stop at leaf): O(n) time | O(n) space
"""




import unittest
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

    def maxDepth1(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Unit Tests


class TestMaxDepth(unittest.TestCase):
    def testMaxDepth1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(
            20, TreeNode(15), TreeNode(7)))
        func = Solution().maxDepth
        func2 = Solution().maxDepth1
        self.assertEqual(func(root=root), 3)
        self.assertEqual(func2(root=root), 3)

    def testMaxDepth2(self):
        root = TreeNode(1, None, TreeNode(2))
        func = Solution().maxDepth
        func2 = Solution().maxDepth1
        self.assertEqual(func(root=root), 2)
        self.assertEqual(func2(root=root), 2)

    def testMaxDepth3(self):
        root = None
        func = Solution().maxDepth
        func2 = Solution().maxDepth1
        self.assertEqual(func(root=root), 0)
        self.assertEqual(func2(root=root), 0)

    def testMaxDepth4(self):
        root = TreeNode(0)
        func = Solution().maxDepth
        func2 = Solution().maxDepth1
        self.assertEqual(func(root=root), 1)
        self.assertEqual(func2(root=root), 1)


if __name__ == "__main__":
    unittest.main()
