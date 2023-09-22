"""
662. Maximum Width of Binary Tree
description: https://leetcode.com/problems/maximum-width-of-binary-tree/description/
"""

"""
Note:
1. BFS + Bitwise: O(n) time | O(2*maxWidth) space - where n is the number of nodes in the tree
"""

import functools
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxWidth = 1
        currentLevel = [(root, 0)] # (node, idx)
        while currentLevel:
            nextLevel = []

            minIdx = float("inf")
            maxIdx = float("-inf")
            for node, idx in currentLevel:
                newIdx = idx * 2
                if node.left:
                    nextLevel.append((node.left, newIdx))
                    minIdx = min(minIdx, newIdx)
                    maxIdx = max(maxIdx, newIdx)
                if node.right:
                    nextLevel.append((node.right, newIdx+1))
                    minIdx = min(minIdx, newIdx+1)
                    maxIdx = max(maxIdx, newIdx+1)
                
            if len(nextLevel) >= 2:
                maxWidth = max(maxWidth, maxIdx-minIdx+1)

            currentLevel = nextLevel
            
        return maxWidth
    
# Unit Tests
import unittest
funcs = [Solution().widthOfBinaryTree]
class TestWidthOfBinaryTree(unittest.TestCase):
    def testWidthOfBinaryTree1(self):
        for widthOfBinaryTree in funcs:
            root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
            self.assertEqual(widthOfBinaryTree(root=root), 4)

    def testWidthOfBinaryTree2(self):
        for widthOfBinaryTree in funcs:
            root = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, TreeNode(7))))
            self.assertEqual(widthOfBinaryTree(root=root), 7)

    def testWidthOfBinaryTree3(self):
        for widthOfBinaryTree in funcs:
            root = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
            self.assertEqual(widthOfBinaryTree(root=root), 2)

if __name__ == "__main__":
    unittest.main()