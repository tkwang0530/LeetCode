"""
1372. Longest ZigZag Path in a Binary Tree
description: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
"""

"""
Note:
1. DFS (postOrder traversal): O(n) time | O(h) space - where n is the number of nodes in the tree and h is the height of the tree
"""

from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        container = [0]
        def dfs(root, container):
            if not root:
                return (0, 0)

            if not root.left and not root.right:
                return (0, 0)

            rlLen, _ = dfs(root.right, container)
            _, lrLen = dfs(root.left, container)

            # go left
            rootLeftLen = rootRightLen = 0
            if root.left:
                rootLeftLen = 1 + lrLen

            # go right
            if root.right:
                rootRightLen = 1 + rlLen

            container[0] = max(container[0], rootLeftLen, rootRightLen)
            return (rootLeftLen, rootRightLen)

        dfs(root, container)
        return container[0]

# Unit Tests
funcs = [Solution().longestZigZag]


class TestLongestZigZag(unittest.TestCase):
    def testLongestZigZag1(self):
        for longestZigZag in funcs:
            root = TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1))))
            self.assertEqual(longestZigZag(root=root), 3)

    def testLongestZigZag2(self):
        for longestZigZag in funcs:
            root = TreeNode(1, TreeNode(1, None, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1))), TreeNode(1))
            self.assertEqual(longestZigZag(root=root), 4)

    def testLongestZigZag3(self):
        for longestZigZag in funcs:
            root = TreeNode(1)
            self.assertEqual(longestZigZag(root=root), 0)

if __name__ == "__main__":
    unittest.main()
