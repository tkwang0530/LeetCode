"""
1038. Binary Search Tree to Greater Sum Tree
description: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
"""

"""
Note:
1. dfs (inorder traversal): O(n) time | O(n) space - where n is the number of nodes in the tree
"""

import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        inorders = []
        def dfs(node):
            if node.left:
                dfs(node.left)

            inorders.append(node)

            if node.right:
                dfs(node.right)

        dfs(root)
        i = len(inorders) - 2
        while i >= 0:
            inorders[i].val += inorders[i+1].val
            i -= 1
        return root

# Unit Tests
funcs = [Solution().bstToGst]

class TestBstToGst(unittest.TestCase):
    def testBstToGst1(self):
        for bstToGst in funcs:
            root = TreeNode(4,  TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
            bstToGst(root)
            self.assertEqual(root.val, 30)
            self.assertEqual(root.left.val, 36)
            self.assertEqual(root.right.val, 21)
            self.assertEqual(root.left.left.val, 36)
            self.assertEqual(root.left.right.val, 35)
            self.assertEqual(root.left.right.right.val, 33)
            self.assertEqual(root.right.left.val, 26)
            self.assertEqual(root.right.right.val, 15)
            self.assertEqual(root.right.right.right.val, 8)

    def testBstToGst2(self):
        for bstToGst in funcs:
            root = TreeNode(0, None, TreeNode(1))
            bstToGst(root)
            self.assertEqual(root.val, 1)
            self.assertEqual(root.right.val, 1)

if __name__ == "__main__":
    unittest.main()
