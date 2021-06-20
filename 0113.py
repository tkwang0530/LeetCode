"""
112. Path Sum
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

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

Outputs: 
[
    [5, 4, 11, 2],
    [5, 8, 4, 5]
]
"""

"""
Note:
1. DFS: O(nlogn) time | O(logn + nlogn) space
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []
        if root is None:
            return paths
        self.dfs(root, sum, [], paths)
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


# Unit Tests


class TestPathSum(unittest.TestCase):
    def testPathSum1(self):
        root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(
            8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
        func = Solution().pathSum
        self.assertEqual(func(root=root, sum=22), [
                         [5, 4, 11, 2], [5, 8, 4, 5]])

    def testPathSum2(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        func = Solution().pathSum
        self.assertEqual(func(root=root, sum=5), [])

    def testPathSum3(self):
        root = TreeNode(1, TreeNode(2), None)
        func = Solution().pathSum
        self.assertEqual(func(root=root, sum=0), [])


if __name__ == "__main__":
    unittest.main()
