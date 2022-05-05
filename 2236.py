"""
2236. Root Equals Sum of Children
You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

Example1:
Input: root = [10,4,6]
Output: true
Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.

Example2:
Input: root = [5,3,1]
Output: false
Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.

Constraints:
The tree consists only of the root, its left child, and its right child.
-100 <= Node.val <= 100
"""

"""
Note:
1. Trial: O(1) time | O(1) space
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)

# Unit Tests
import unittest
funcs = [Solution().checkTree]

class TestCheckTree(unittest.TestCase):
    def testCheckTree1(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(3), TreeNode(1))
            self.assertEqual(func(root=root), False)

    def testCheckTree2(self):
        for func in funcs:
            root = TreeNode(10, TreeNode(4), TreeNode(6))
            self.assertEqual(func(root=root), True)

if __name__ == "__main__":
    unittest.main()
