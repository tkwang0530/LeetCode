"""
2641. Cousins in Binary Tree II
description: https://leetcode.com/problems/cousins-in-binary-tree-ii/description/
"""

"""
Note:
1. BFS (Layer Order Traversal): O(n) time | O(n) space - where n is the number of nodes in the tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currentLayer = [(root, None)]
        while currentLayer:
            nextLayer = []
            currentSum = 0
            parentSums = collections.defaultdict(int)
            for node, p in currentLayer:
                parentSums[p] += node.val
                currentSum += node.val
                if node.left:
                    nextLayer.append((node.left, node))
                if node.right:
                    nextLayer.append((node.right, node))

            for node, p in currentLayer:
                node.val = currentSum - parentSums[p]
            
            currentLayer = nextLayer
        return root

import unittest
funcs = [Solution().replaceValueInTree]
class TestReplaceValueInTree(unittest.TestCase):
    def testReplaceValueInTree1(self):
        for func in funcs:
            node5 = TreeNode(5)
            node4, node9 = TreeNode(4), TreeNode(9)
            node1, node10 = TreeNode(1), TreeNode(10)
            node7 = TreeNode(7)
            node5.left, node5.right = node4, node9
            node4.left, node4.right = node1, node10
            node9.right = node7

            root = node5
            func(root=root)
            self.assertEqual(node5.val, 0)
            self.assertEqual(node4.val, 0)
            self.assertEqual(node9.val, 0)

            self.assertEqual(node1.val, 7)

            self.assertEqual(node10.val, 7)
            self.assertEqual(node7.val, 11)

    def testReplaceValueInTree2(self):
        for func in funcs:
            node3 = TreeNode(3)
            node1, node2 = TreeNode(1), TreeNode(2)
            node3.left, node3.right = node1, node2
            
            root = node3
            func(root=root)
            self.assertEqual(node3.val, 0)
            self.assertEqual(node1.val, 0)
            self.assertEqual(node2.val, 0)

if __name__ == "__main__":
    unittest.main()
