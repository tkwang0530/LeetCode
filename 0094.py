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
inorder: left -> self -> right 
do it reversely => right -> self -> left

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
        if root is None:
            return []
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if visited:
                res.append(node.val)
            else:  # inorder left -> root -> right
                if node.right is not None:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left is not None:
                    stack.append((node.left, False))
        return res

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


class TestInorderTraversal(unittest.TestCase):
    def testInorderTraversal1(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
        func = Solution().inorderTraversal
        func2 = Solution().inorderTraversal2
        self.assertEqual(func(root=root), [1, 3, 2])
        self.assertEqual(func2(root=root), [1, 3, 2])

    def testInorderTraversal2(self):
        root = None
        func = Solution().inorderTraversal
        func2 = Solution().inorderTraversal2
        self.assertEqual(func(root=root), [])
        self.assertEqual(func2(root=root), [])

    def testInorderTraversal3(self):
        root = TreeNode(1)
        func = Solution().inorderTraversal
        func2 = Solution().inorderTraversal2
        self.assertEqual(func(root=root), [1])
        self.assertEqual(func2(root=root), [1])

    def testInorderTraversal4(self):
        root = TreeNode(1, TreeNode(2))
        func = Solution().inorderTraversal
        func2 = Solution().inorderTraversal2
        self.assertEqual(func(root=root), [2, 1])
        self.assertEqual(func2(root=root), [2, 1])

    def testInorderTraversal5(self):
        root = TreeNode(1, None, TreeNode(2))
        func = Solution().inorderTraversal
        func2 = Solution().inorderTraversal2
        self.assertEqual(func(root=root), [1, 2])
        self.assertEqual(func2(root=root), [1, 2])


if __name__ == "__main__":
    unittest.main()
