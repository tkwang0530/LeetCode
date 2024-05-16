"""
2331. Evaluate Boolean Binary Tree
description: https://leetcode.com/problems/evaluate-boolean-binary-tree/description/
"""

"""
Note:
1. Recursion: O(n) time | O(h) space - where n is the number of nodes in the tree and h is the height of the tree
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True if root.val == 1 else False

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)


# Unit Tests
import unittest
funcs = [Solution().evaluateTree]

class TestEvaluateTree(unittest.TestCase):
    def testEvaluateTree1(self):
        for func in funcs:
            root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
            self.assertEqual(func(root), True)

    def testEvaluateTree2(self):
        for func in funcs:
            root = TreeNode(0)
            self.assertEqual(func(root), False)

if __name__ == "__main__":
    unittest.main()