"""
513. Find Bottom Left Tree Value
description: https://leetcode.com/problems/find-bottom-left-tree-value/description/
"""

"""
Note:
1. BFS (layer order traversal): O(n) time | O(n) space - where n is the number of nodes in the binary tree
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # bfs (layer order traversal)
        candidate = root.val
        currentNodes = [root]
        while currentNodes:
            nextNodes = []
            for i, node in enumerate(currentNodes):
                if i == 0:
                    candidate = node.val
                
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            
            currentNodes = nextNodes
        return candidate

# Unit Tests
import unittest
funcs = [Solution().findBottomLeftValue]

class TestFindBottomLeftValue(unittest.TestCase):
    def testFindBottomLeftValue1(self):
        for func in funcs:
            root = TreeNode(2, TreeNode(1), TreeNode(3))
            self.assertEqual(func(root=root), 1)

    def testFindBottomLeftValue2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))
            self.assertEqual(func(root=root), 7)

if __name__ == "__main__":
    unittest.main()
