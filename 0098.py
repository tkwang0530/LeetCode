"""
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example1:
            2
          /    \
        1       3
Input: root = [2, 1, 3]
Output: true

Example2:
            5
        /        \
      1          4
                /    \
              3       6
Input: root = [5, 1, 4, null, null, 3, 6]
Output: false
Explanation: The node's value is 5 but its right child's value is 4.
"""

"""
Note:
1. Recursive solution: O(n) time | O(n) space
validateBstHelper(root, minValue, maxValue)
2. Iterative solution: O(n) time | O(n) space
"""




import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validateBstHelper(root, float("-inf"), float("inf"))

    def validateBstHelper(self, root: TreeNode, minValue, maxValue) -> bool:
        if root is None:
            return True
        rootIsValid = root.val < maxValue and root.val > minValue
        leftIsValid = self.validateBstHelper(root.left, minValue, root.val)
        rightIsValid = self.validateBstHelper(root.right, root.val, maxValue)
        return rootIsValid and leftIsValid and rightIsValid

    def isValidBST2(self, root: TreeNode) -> bool:
        stack = []
        pre = None
        while root is not None or len(stack) > 0:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre is not None and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True


# Unit Tests
funcs = [Solution().isValidBST, Solution().isValidBST2]


class TestIsValidBST(unittest.TestCase):
    def testIsValidBST1(self):
        for func in funcs:
            root = TreeNode(2, TreeNode(1), TreeNode(3))
            self.assertEqual(func(root=root), True)

    def testIsValidBST2(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(1), TreeNode(
                4, TreeNode(3), TreeNode(6)))
            self.assertEqual(func(root=root), False)


if __name__ == "__main__":
    unittest.main()
