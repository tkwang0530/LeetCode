"""
988. Smallest String Starting From Leaf
description: https://leetcode.com/problems/smallest-string-starting-from-leaf/description/
"""

"""
Note:
1. backtracking + Sort: O(nlogn) time | O(n) space - where n is the number of nodes in the tree
2. backtracking: O(n) time | O(n) space
"""


import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        chars = []
        candidates = []
        def backtrack(root):
            chars.append(chr(ord("a")+root.val))
            if not root.left and not root.right:
                candidates.append("".join(chars[::-1]))
            if root.left:
                backtrack(root.left)
            if root.right:
                backtrack(root.right)
            chars.pop()
        
        backtrack(root)
        candidates.sort()
        return candidates[0]

class Solution2:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        chars = []
        container = [chr(ord("z")+1)]
        def backtrack(root):
            chars.append(chr(ord("a")+root.val))
            if not root.left and not root.right:
                container[0] = min(container[0], "".join(chars[::-1]))
            if root.left:
                backtrack(root.left)
            if root.right:
                backtrack(root.right)
            chars.pop()
        
        backtrack(root)
        return container[0]

# Unit Tests
funcs = [Solution().smallestFromLeaf, Solution2().smallestFromLeaf]


class TestSmallestFromLeaf(unittest.TestCase):
    def testSmallestFromLeaf1(self):
        for func in funcs:
            root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
            self.assertEqual(func(root=root), "dba")

    def testSmallestFromLeaf2(self):
        for func in funcs:
            root = TreeNode(25, TreeNode(1, TreeNode(1)), TreeNode(3, TreeNode(0), TreeNode(2)))
            self.assertEqual(func(root=root), "adz")


    def testSmallestFromLeaf3(self):
        for func in funcs:
            root = TreeNode(2, TreeNode(2, TreeNode(1, TreeNode(0)), TreeNode(1)), TreeNode(1, TreeNode(0)))
            self.assertEqual(func(root=root), "abc")


if __name__ == "__main__":
    unittest.main()
