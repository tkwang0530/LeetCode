"""
102. Binary Tree Level Order Traversal
description: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""

"""
Note:
1. BFS (layer order traversal): O(n) time | O(n) space - where n is the number of nodes in the tree
"""




from typing import List, Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output = []
        currentNodes = [root]
        while currentNodes:
            nextNodes = []
            levelVals = []
            for node in currentNodes:
                levelVals.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            output.append(levelVals)
            currentNodes = nextNodes
        return output

# Unit Tests

funcs = [Solution().levelOrder]
class TestLevelOrder(unittest.TestCase):
    def testLevelOrder1(self):
        for levelOrder in funcs:
            root = TreeNode(3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)))
            self.assertEqual(levelOrder(root=root), [[3], [9, 20], [15, 7]])

    def testLevelOrder2(self):
        for levelOrder in funcs:
            root = TreeNode(1)
            self.assertEqual(levelOrder(root=root), [[1]])

    def testLevelOrder3(self):
        for levelOrder in funcs:
            root = None
            self.assertEqual(levelOrder(root=root), [])


if __name__ == "__main__":
    unittest.main()
