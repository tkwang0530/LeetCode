"""
623. Add One Row to Tree
description: https://leetcode.com/problems/add-one-row-to-tree/description/
"""

"""
Note:
1. Recursive DFS (PostOrder Traversal): O(n) time | O(h) space
"""

from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return node
    
            if depth == 1:
                newRoot = TreeNode(val)
                newRoot.left = node
                return newRoot
            
            if depth == 2:
                leftSubTree = node.left
                node.left = TreeNode(val)
                node.left.left = leftSubTree
                rightSubTree = node.right
                node.right = TreeNode(val)
                node.right.right = rightSubTree
                return node
            
            node.left = dfs(node.left, depth-1)
            node.right = dfs(node.right, depth-1)
            return node
        return dfs(root, depth)

# Unit Tests
funcs = [Solution().addOneRow]


class TestAddOneRow(unittest.TestCase):
    def testAddOneRow1(self):
        for func in funcs:
            root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
            newRoot = func(root=root, val=1, depth=2)
            self.assertEqual(newRoot.left.val, 1)
            self.assertEqual(newRoot.right.val, 1)
            self.assertEqual(newRoot.left.left.val, 2)
            self.assertEqual(newRoot.left.left.left.val, 3)
            self.assertEqual(newRoot.left.left.right.val, 1)
            self.assertEqual(newRoot.right.right.val, 6)
            self.assertEqual(newRoot.right.right.left.val, 5)

    def testAddOneRow2(self):
        for func in funcs:
            root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)))
            newRoot = func(root=root, val=1, depth=3)
            self.assertEqual(newRoot.left.val, 2)
            self.assertEqual(newRoot.left.left.val, 1)
            self.assertEqual(newRoot.left.right.val, 1)
            self.assertEqual(newRoot.left.left.left.val, 3)
            self.assertEqual(newRoot.left.right.right.val, 1)

if __name__ == "__main__":
    unittest.main()
