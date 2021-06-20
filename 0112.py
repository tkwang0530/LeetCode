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
"""




import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
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

        dfs(root, sum)
        return result[0]


# Unit Tests


class TestHasPathSum(unittest.TestCase):
    def testHasPathSum1(self):
        root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(
            8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
        func = Solution().hasPathSum
        self.assertEqual(func(root=root, sum=22), True)

    def testHasPathSum2(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        func = Solution().hasPathSum
        self.assertEqual(func(root=root, sum=5), False)

    def testHasPathSum3(self):
        root = TreeNode(1, TreeNode(2))
        func = Solution().hasPathSum
        self.assertEqual(func(root=root, sum=0), False)


if __name__ == "__main__":
    unittest.main()
