"""
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example1:
Input: root = [1, null, 2, 3]
            1
                \
                 2
                /
            3

Output: [1, 3, 2] 

Example2:
Input: root = []
Output: []

Example3:
Input: root = [1]
Output: [1]

Example4:
Input: root = [1, 2]
Output: [2, 1]

Example5:
Input: root = [1, null, 2]
Output: [1, 2]
"""

"""
Note:
1. Iterative solution: O(n) time | O(n) space
2. Recursive solution: O(n) time | O(n) space
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        while root is not None or len(stack) > 0:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        self.dfs(root, res)
        return res

    def dfs(self, root: TreeNode, res: List[int]):
        if root.left is not None:
            self.dfs(root.left, res)
        res.append(root.val)
        if root.right is not None:
            self.dfs(root.right, res)


# Unit Tests
funcs = [Solution().inorderTraversal, Solution().inorderTraversal2]


class TestInorderTraversal(unittest.TestCase):
    def testInorderTraversal1(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
            self.assertEqual(func(root=root), [1, 3, 2])

    def testInorderTraversal2(self):
        for func in funcs:
            root = None
            self.assertEqual(func(root=root), [])

    def testInorderTraversal3(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), [1])

    def testInorderTraversal4(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2))
            self.assertEqual(func(root=root), [2, 1])

    def testInorderTraversal5(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2))
            self.assertEqual(func(root=root), [1, 2])


if __name__ == "__main__":
    unittest.main()
