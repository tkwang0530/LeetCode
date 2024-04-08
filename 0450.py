"""
450. Delete Node in a BST
description: https://leetcode.com/problems/delete-node-in-a-bst/description/
"""

"""
Note:
1. dfs: O(h) time | O(h) space - where h is the height of the tree
ref: https://www.youtube.com/watch?v=LFzAoJJt92M
"""


from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Find the min from right subtree
            current = root.right
            while current.left:
                current = current.left
            root.val = current.val
            root.right = self.deleteNode(root.right, root.val)
        return root

# Unit Tests
funcs = [Solution().deleteNode]


class TestDeleteNode(unittest.TestCase):
    def testDeleteNode1(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
            root = func(root=root, key=3)
            self.assertEqual(root.val, 5)
            self.assertEqual(root.left.val, 4)
            self.assertEqual(root.left.left.val, 2)
            self.assertEqual(root.left.right, None)
            self.assertEqual(root.right.val, 6)
            self.assertEqual(root.right.right.val, 7)

    def testDeleteNode2(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
            root = func(root=root, key=5)
            self.assertEqual(root.val, 6)
            self.assertEqual(root.left.val, 3)
            self.assertEqual(root.left.left.val, 2)
            self.assertEqual(root.left.right.val, 4)
            self.assertEqual(root.right.val, 7)

    def testDeleteNode3(self):
        for func in funcs:
            root = None
            root = func(root=root, key=0)
            self.assertEqual(root, None)


if __name__ == "__main__":
    unittest.main()
