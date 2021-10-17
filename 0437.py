"""
437. Path Sum III
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000
"""

"""
Note:
1. Recursive DFS: O(n^2) time | O(n) space
no need to be a leaf node
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def dfs(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        targetSum -= root.val
        return (1 if targetSum == 0 else 0) + self.dfs(root.left, targetSum) + self.dfs(root.right, targetSum)


# Unit Tests
import unittest
funcs = [Solution().pathSum]

class TestPathSum(unittest.TestCase):
    def testPathSum1(self):
        for func in funcs:
            root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
            self.assertEqual(func(root=root, targetSum=8), 3)

    def testPathSum2(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13, TreeNode(5), TreeNode(1)), TreeNode(4)))
            self.assertEqual(func(root=root, targetSum=22), 3)

    def testPathSum3(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2), None))
            self.assertEqual(func(root=root, targetSum=-1), 4)

if __name__ == "__main__":
    unittest.main()
