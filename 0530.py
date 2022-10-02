"""
530. Minimum Absolute Difference in BST
Given the root of a Binary Search Tree (BST), return tthe minimum absolute difference between the values of any two different nodes in the tree.

Example1:
Input: root = [4,2,6,1,3]
Output: 1

Example2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 10^4].
0 <= Node.val <= 10^5
"""

"""
Note:
1. Morris traversal: O(n) time | O(1) space - where n is the number of nodes in the tree
"""




from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = float("-inf")
        minDiff = float("inf")
        current = root
        while current:
            if not current.left:
                minDiff = min(minDiff, abs(current.val - prev))
                prev = current.val
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    minDiff = min(minDiff, abs(current.val - prev))
                    prev = current.val
                    current = current.right
        return minDiff


# Unit Tests
funcs = [Solution().getMinimumDifference]


class TestGetMinimumDifference(unittest.TestCase):
    def testGetMinimumDifference1(self):
        for func in funcs:
            root = TreeNode(4, TreeNode(
                2, TreeNode(1), TreeNode(3)), TreeNode(6))
            self.assertEqual(func(root=root), 1)

    def testGetMinimumDifference2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(0), TreeNode(
                48, TreeNode(12), TreeNode(49)))
            self.assertEqual(func(root=root), 1)


if __name__ == "__main__":
    unittest.main()
