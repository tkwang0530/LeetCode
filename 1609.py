"""
1609. Even Odd Tree
description: https://leetcode.com/problems/even-odd-tree/description/
"""

"""
Note:
1. BFS (layer order traversal): O(n) time | O(n) space - where n is the number of nodes in the tree
"""

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val % 2 == 0:
            return False

        currentLayer = [root]
        isEvenLevel = False

        def invalid(isEvenLevel, nextLayerNode, node):
            if isEvenLevel and node and node.val % 2 == 0:
                return True

            if not isEvenLevel and node and node.val % 2 > 0:
                return True
            
            if isEvenLevel and nextLayerNode and nextLayerNode.val >= node.val:
                return True

            if not isEvenLevel and nextLayerNode and nextLayerNode.val <= node.val:
                return True

            return False
        
        while currentLayer:
            nextLayer = []
            for node in currentLayer:
                if node.left:
                    nextLayerNode = nextLayer[-1] if nextLayer else None
                    if invalid(isEvenLevel, nextLayerNode, node.left):
                        return False

                    nextLayer.append(node.left)

                if node.right:
                    nextLayerNode = nextLayer[-1] if nextLayer else None
                    if invalid(isEvenLevel, nextLayerNode, node.right):
                        return False

                    nextLayer.append(node.right)

            
            isEvenLevel = not isEvenLevel
            currentLayer = nextLayer
        return True

# Unit Tests
import unittest
funcs = [Solution().isEvenOddTree]

class TestIsEvenOddTree(unittest.TestCase):
    def testIsEvenOddTree1(self):
        for isEvenOddTree in funcs:
            root = TreeNode(1, TreeNode(10, TreeNode(3, TreeNode(12), TreeNode(8))), TreeNode(4, TreeNode(7, TreeNode(6)), TreeNode(9, None, TreeNode(2))))
            self.assertEqual(isEvenOddTree(root=root), True)

    def testIsEvenOddTree2(self):
        for isEvenOddTree in funcs:
            root = TreeNode(5, TreeNode(4, TreeNode(3), TreeNode(3)), TreeNode(2, TreeNode(7)))
            self.assertEqual(isEvenOddTree(root=root), False)

    def testIsEvenOddTree3(self):
        for isEvenOddTree in funcs:
            root = TreeNode(5, TreeNode(9, TreeNode(3), TreeNode(5)), TreeNode(1, TreeNode(7)))
            self.assertEqual(isEvenOddTree(root=root), False)

if __name__ == "__main__":
    unittest.main()