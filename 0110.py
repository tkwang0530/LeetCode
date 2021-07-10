"""
110. Balanced Binary Tree
Given a binary tree, determin if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
- a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example1:
            3
         /      \
      3         20
                /    \
            15       7
Input: root = [3, 9, 20, null, null, 15, 7]
Output: true

Example2:
                    1
                  /    \
                2      2
              /    \
            3      3
          /    \
        3      4
Input: root = [1, 2, 2, 3, 3, null, null, 4, 4]
Output: false

Example3:
Input: root = []
Output: true
"""

"""
Note:
1. Recursion (track heights, isBalanced): O(n) time | O(h) space
2. Iteration (track last visit node, heights): O(n) time | O(h) space
"""




import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, isBalanced: bool, height: int):
        self.isBalanced = isBalanced
        self.height = height


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root).isBalanced

    def helper(self, root: TreeNode) -> TreeInfo:
        if not root:
            return TreeInfo(True, 0)
        leftTreeInfo = self.helper(root.left)
        rightTreeInfo = self.helper(root.right)
        return TreeInfo(abs(leftTreeInfo.height - rightTreeInfo.height) <= 1 and leftTreeInfo.isBalanced and rightTreeInfo.isBalanced, 1 + max(leftTreeInfo.height, rightTreeInfo.height))

    def isBalanced2(self, root: TreeNode) -> bool:
        stack, node, last, heights = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = heights.get(
                        node.left, 0), heights.get(node.right, 0)
                    if abs(left - right) > 1:
                        return False
                    heights[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True


# Unit Tests
funcs = [Solution().isBalanced, Solution().isBalanced2]


class TestIsBalanced(unittest.TestCase):
    def testIsBalanced1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)))
            self.assertEqual(func(root=root), True)

    def testIsBalanced2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(
                3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
            self.assertEqual(func(root=root), False)

    def testIsBalanced3(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
            self.assertEqual(func(root=root), False)


if __name__ == "__main__":
    unittest.main()
