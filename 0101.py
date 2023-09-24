"""
101. Symmetric Tree
description: https://leetcode.com/problems/symmetric-tree/description/
"""

"""
Note:
1. Recursion (DFS postorder traversal): O(n) time | O(h) space - where n is the number of nodes in the tree and h is the height of the tree
2. Iteration (DFS preorder traversal): O(n) time | O(n) space - where n is the number of nodes in the tree
"""


import unittest
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isReverse(tree1, tree2):
            if not tree1 and not tree2:
                return True

            if None in (tree1, tree2):
                return False

            return tree1.val == tree2.val and isReverse(tree1.left, tree2.right) and isReverse(tree1.right, tree2.left)

        return isReverse(root.left, root.right)

class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True


# Unit Tests
funcs = [Solution().isSymmetric, Solution2().isSymmetric]

class TestIsSymmetric(unittest.TestCase):
    def testIsSymmetric1(self):
        for isSymmetric in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(
                4)), TreeNode(2, TreeNode(4), TreeNode(3)))
            self.assertEqual(isSymmetric(root=root), True)

    def testIsSymmetric2(self):
        for isSymmetric in funcs:
            root = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                            TreeNode(2, None, TreeNode(3)))
            self.assertEqual(isSymmetric(root=root), False)


if __name__ == "__main__":
    unittest.main()
