"""
145. Binary Tree Postorder Traversal
Given the root of a binary tree, return the postorder traversal of its node's values.

Example1:
        1
           \
            2
          /
        3
Input: root = [1, null, 2, 3]
Output: [3, 2, 1]

Example2:
Input: root = []
Output: []

Example3:
Input: root = [1]
Output: [1]

Example4:
        1
      /
    2
Input: root = [1,2]
Output: [2,1]

Example5:
    1
       \
        2
Input: root = [1,null,2]
Output: [2,1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trival, could you do it iteratively?
"""

"""
Note:
1. Recursion: O(n) time | O(h) space
2. Iteration (PreOrder like traversal then reverse the result): O(n) time | O(h) space
visited root -> right -> left
3. Iteration (track visited node with tuple): O(n) time | O(n) space
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        self.dfs(root, result)
        return result

    def dfs(self, root: TreeNode, result: List[int]):
        if root.left:
            self.dfs(root.left, result)
        if root.right:
            self.dfs(root.right, result)
        result.append(root.val)

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        result, stack = [], [root]
        if not root:
            return result
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        result, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    result.append(node.val)
                else:
                    # post-order (reversely)
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return result


# Unit Tests
funcs = [Solution().postorderTraversal, Solution(
).postorderTraversal2, Solution().postorderTraversal3]


class TestPostorderTraversal(unittest.TestCase):
    def testPostorderTraversal1(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
            self.assertEqual(func(root=root), [3, 2, 1])

    def testPostorderTraversal2(self):
        for func in funcs:
            root = None
            self.assertEqual(func(root=root), [])

    def testPostorderTraversal3(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), [1])

    def testPostorderTraversal4(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2))
            self.assertEqual(func(root=root), [2, 1])

    def testPostorderTraversal4(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2))
            self.assertEqual(func(root=root), [2, 1])


if __name__ == "__main__":
    unittest.main()
