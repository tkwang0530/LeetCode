"""
543. Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example1:
        1
      /   \
    2     3 
  /    \
4      5
Input: root = [1,2,3, 4, 5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example2:
Input: root = [1, 2]
Output: 1
"""

"""
Note:
1. Recursion with TreeInfo: O(n) time | O(n) space
TreeInfo stores diameter, height
diameter = max(pathThroughRoot, maxPathNotThroughRoot)
height = 1 + max(left.height, right.height)
"""




import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diameter: int, height: int):
        self.diameter = diameter
        self.height = height


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.helper(root).diameter

    def helper(self, root: TreeNode) -> TreeInfo:
        if not root:
            return TreeInfo(0, 0)

        leftTreeInfo = self.helper(root.left)
        rightTreeInfo = self.helper(root.right)

        pathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
        maxPathNotThroughRoot = max(
            leftTreeInfo.diameter, rightTreeInfo.diameter)
        return TreeInfo(max(pathThroughRoot, maxPathNotThroughRoot), 1 + max(leftTreeInfo.height, rightTreeInfo.height))


# Unit Tests
funcs = [Solution().diameterOfBinaryTree]


class TestDiameterOfBinaryTree(unittest.TestCase):
    def testDiameterOfBinaryTree1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(
                2, TreeNode(4), TreeNode(5)), TreeNode(3))
            self.assertEqual(func(root=root), 3)

    def testDiameterOfBinaryTree2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2))
            self.assertEqual(func(root=root), 1)


if __name__ == "__main__":
    unittest.main()
