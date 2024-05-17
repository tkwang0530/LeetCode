"""
1325. Delete Leaves With a Given Value
description: https://leetcode.com/problems/delete-leaves-with-a-given-value/description/
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
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        
        return None if (root.val == target and not root.left and not root.right) else root

# Unit Tests
import unittest
funcs = [Solution().removeLeafNodes]

class TestRemoveLeafNodes(unittest.TestCase):
    def testRemoveLeafNodes1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(2), None), TreeNode(3, TreeNode(2), TreeNode(4)))
            target = 2
            newRoot = func(root=root, target=target)
            self.assertEqual(newRoot.val, 1)
            self.assertEqual(newRoot.left, None)
            self.assertEqual(newRoot.right.val, 3)
            self.assertEqual(newRoot.right.left, None)
            self.assertEqual(newRoot.right.right.val, 4)

    def testRemoveLeafNodes2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(3, TreeNode(3), TreeNode(2)), TreeNode(3))
            target = 3
            newRoot = func(root=root, target=target)
            self.assertEqual(newRoot.val, 1)
            self.assertEqual(newRoot.left.val, 3)
            self.assertEqual(newRoot.right, None)
            self.assertEqual(newRoot.left.right.val, 2)
            self.assertEqual(newRoot.left.left, None)

    def testRemoveLeafNodes3(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(2, TreeNode(2)), ))
            target = 2
            newRoot = func(root=root, target=target)
            self.assertEqual(newRoot.val, 1)
            self.assertEqual(newRoot.left, None)
            self.assertEqual(newRoot.right, None)


if __name__ == "__main__":
    unittest.main()
