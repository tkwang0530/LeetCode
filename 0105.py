"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
Return the following binary tree:
        3
      /    \
    9     20
           /   \
         15     7  
"""

"""
Note:
1. Tree Construction - Top Down: O(n) time | O(n + h) space
preorder: self left right
inorder: left self right
preprocessing: map a value to its index in inorder list
map: { 9: 0, 3: 1, 15:2, 20:3, 7:4}
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        map = {}
        for i in range(len(inorder)):
            map[inorder[i]] = i
        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, map)

    def helper(self, P, startP, endP, I, startI, endI, map) -> TreeNode:
        if startP > endP:
            return None
        rootNode = TreeNode(P[startP])
        rootIndex = map[P[startP]]  # get index of rootNode in I
        numLeft = rootIndex - startI
        rootNode.left = self.helper(
            P, startP + 1, startP + numLeft, I, startI, rootIndex - 1, map)
        rootNode.right = self.helper(
            P, startP + numLeft + 1, endP, I, rootIndex + 1, endI, map)
        return rootNode

# Unit Tests


class TestBuildTree(unittest.TestCase):
    def testBuildTree1(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        func = Solution().buildTree
        buildedTreeRoot = func(preorder=preorder, inorder=inorder)
        self.assertEqual(buildedTreeRoot.val, 3)
        self.assertEqual(buildedTreeRoot.left.val, 9)
        self.assertEqual(buildedTreeRoot.right.val, 20)
        self.assertEqual(buildedTreeRoot.right.left.val, 15)
        self.assertEqual(buildedTreeRoot.right.right.val, 7)


if __name__ == "__main__":
    unittest.main()
