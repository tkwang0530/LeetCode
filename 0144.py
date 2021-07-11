"""
144. Binary Tree Preorder Traversal
Given a binary tree, return preorder traversal of its nodes' values.


Example1:
Input: root = [1, null, 2, 3], 
            1
               \
                 2
               /
            3  

Outputs: [1, 2, 3]
Follow up: Recursive solution is trival, could you do it iteratively?
"""

"""
Note:
1. DFS (Iterative Boundary Walk): O(n) time | O(n) space
use explicit stack (LIFO)
2. Morris Traversal: O(n) time | O(1) space
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        stack = [root]
        while len(stack) != 0:
            treeNode = stack.pop()
            result.append(treeNode.val)
            if treeNode.right is not None:
                stack.append(treeNode.right)
            if treeNode.left is not None:
                stack.append(treeNode.left)
        return result

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        current = root
        result = []
        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right != current and predecessor.right is not None:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = current
                    result.append(current.val)
                    current = current.left
                else:
                    predecessor.right = None
                    current = current.right
        return result

# Unit Tests


funcs = [Solution().preorderTraversal, Solution().preorderTraversal2]


class TestPreorderTraversal(unittest.TestCase):
    def testPreorderTraversal1(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
            self.assertEqual(func(root=root), [1, 2, 3])

    def testPreorderTraversal2(self):
        for func in funcs:
            root = None
            self.assertEqual(func(root=root), [])

    def testPreorderTraversal3(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), [1])


if __name__ == "__main__":
    unittest.main()
