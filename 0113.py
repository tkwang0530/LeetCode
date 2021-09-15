"""
113. Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example1:
Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], sum = 22
            5
         /      \
      4          8
    /            /   \
  11         13    4
  /  \                   \
7    2                    1

Outputs: 
[
    [5, 4, 11, 2],
    [5, 8, 4, 5]
]
"""

"""
Note:
1. Recursive DFS: O(n^2) time | O(h) space
2. Iterative DFS with stack and Hash Table: O(n^2) time | O(h) space
"""

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []
        if root is None:
            return paths
        self.dfs(root, targetSum, [], paths)
        return paths

    def dfs(self, treeNode: TreeNode, target: int, path: List[int], paths: List[List[int]]):
        path.append(treeNode.val)
        if treeNode.left is None and treeNode.right is None:  # leaf
            if treeNode.val == target:
                paths.append(path.copy())
        if treeNode.left is not None:
            self.dfs(treeNode.left, target - treeNode.val, path, paths)
        if treeNode.right is not None:
            self.dfs(treeNode.right, target - treeNode.val, path, paths)
        path.pop()

    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return result
        path, stack, currentSum = [], [root], 0
        visited = set()
        while stack:
            node = stack[-1]
            if node in visited:
                stack.pop()
                currentSum -= node.val
                path.pop()
                continue
            visited.add(node)
            path.append(node.val)
            currentSum += node.val

            if not node.left and not node.right:
                if currentSum == targetSum:
                    result.append(path[:])
                path.pop()
                stack.pop()
                currentSum -= node.val
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result
        

# Unit Tests
import unittest
funcs = [Solution().pathSum, Solution().pathSum2]

class TestPathSum(unittest.TestCase):
    def testPathSum1(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(
                8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
            self.assertEqual(func(root=root, targetSum=22), [
                            [5, 4, 11, 2], [5, 8, 4, 5]])

    def testPathSum2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2), TreeNode(3))
            self.assertEqual(func(root=root, targetSum=5), [])

    def testPathSum3(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2), None)
            self.assertEqual(func(root=root, targetSum=0), [])


if __name__ == "__main__":
    unittest.main()
