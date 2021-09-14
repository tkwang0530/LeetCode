"""
112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example1:
Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], sum = 22
            5
         /      \
      4          8
    /            /   \
  11         13    4
  /  \                   \
7    2                    1

Outputs: true
"""

"""
Note:
1. DFS: O(n) time | O(h) space
2. DFS (Preorder Traversal): O(n) time | O(h) space
"""

from typing import Optional
from collections import deque
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        result = [False]  # list is mutable

        def dfs(treeNode: TreeNode, target: int) -> bool:
            if treeNode.left is None and treeNode.right is None:
                if treeNode.val == target:
                    result[0] = True
            if treeNode.left is not None:
                dfs(treeNode.left, target - treeNode.val)
            if treeNode.right is not None:
                dfs(treeNode.right, target - treeNode.val)

        dfs(root, targetSum)
        return result[0]

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum)]
        while stack:
            node, targetSum = stack.pop()
            if not node.left and not node.right and node.val == targetSum:
                return True
            if node.right:
                stack.append((node.right, targetSum - node.val))
            if node.left:
                stack.append((node.left, targetSum - node.val))
        return False

    def hasPathSum3(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, targetSum)])
        while queue:
            node, targetSum = queue.popleft()
            if not node.left and not node.right and node.val == targetSum:
                return True
            else:
                if node.left:
                    queue.append((node.left, targetSum - node.val))
                if node.right:
                    queue.append((node.right, targetSum - node.val))
        return False


# Unit Tests
funcs = [Solution().hasPathSum, Solution().hasPathSum2, Solution().hasPathSum3]


class TestHasPathSum(unittest.TestCase):
    def testHasPathSum1(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(
                8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
            self.assertEqual(func(root=root, targetSum=22), True)

    def testHasPathSum2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2), TreeNode(3))
            self.assertEqual(func(root=root, targetSum=5), False)

    def testHasPathSum3(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2))
            self.assertEqual(func(root=root, targetSum=0), False)


if __name__ == "__main__":
    unittest.main()
