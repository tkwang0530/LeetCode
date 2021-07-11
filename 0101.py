"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example1:
            1
         /      \
      2          2
    /    \      /    \
  3      4   3      4
Input: root = [1,2,2,3,4,4,3]
Output: true

Example2:
            1
         /      \
      2          2
         \          \
          3          3
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

"""
Note:
1. Recursion (DFS): O(n) time | O(logn) space
2. Iteration (DFS): O(n) time | O(logn) space
"""




import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False

    def isSymmetric2(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True


# Unit Tests
funcs = [Solution().isSymmetric, Solution().isSymmetric2]


class TestIsSymmetric(unittest.TestCase):
    def testIsSymmetric1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(
                4)), TreeNode(2, TreeNode(4), TreeNode(3)))
            self.assertEqual(func(root=root), True)

    def testIsSymmetric2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                            TreeNode(2, None, TreeNode(3)))
            self.assertEqual(func(root=root), False)


if __name__ == "__main__":
    unittest.main()
