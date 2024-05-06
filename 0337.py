"""
337. House Robber III
description: https://leetcode.com/problems/house-robber-iii/description/
"""

"""
Note:
1. dfs+memo: O(n) time | O(n) space - where n is the number of nodes in the tree
"""

import functools
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @functools.lru_cache(None)
        def dfs(node: TreeNode, isSafe: bool) -> int:
            if not node:
                return 0

            maxAmount = 0
            # skip
            maxAmount = max(maxAmount, dfs(node.left, True)+dfs(node.right, True))

            # rob if isSafe
            if isSafe:
                maxAmount = max(maxAmount, node.val + dfs(node.left, False)+dfs(node.right, False))

            return maxAmount
        return dfs(root, True)


# Unit Tests
funcs = [Solution().rob]


class TestRob(unittest.TestCase):
    def testRob1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
            self.assertEqual(func(root), 7)

    def testRob2(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
            self.assertEqual(func(root), 9)


if __name__ == "__main__":
    unittest.main()
