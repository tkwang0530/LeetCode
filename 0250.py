"""
250. Count Univalue Subtrees
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.
Note: all lead nodes are uni-value subtrees
Example1:
Input: root = [5, 1, 5, 5, 5, null, 5], 
            5
         /      \
      1          5
    /   \            \
  5     5           5

Outputs: 4
"""

"""
Note:
1. DFS (Bottom-Up with List): O(n) time | O(h) space
2. DFS (Bottom-Up with Tuple): O(n) time | O(h) space
"""




from typing import List
from typing import Tuple
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None:
            return 0
        result = [0]
        self.dfs(root, result)
        return result[0]

    def dfs(self, treeNode: TreeNode, result: List[int]) -> bool:
        if treeNode.left is None and treeNode.right is None:  # leaf
            result[0] += 1
            return True  # leaf is always unival
        amIUniVal = True
        if treeNode.left is not None:
            isLeftUniVal = self.dfs(treeNode.left, result)
            if not isLeftUniVal or treeNode.val != treeNode.left.val:
                amIUniVal = False

        if treeNode.right is not None:
            isRightUniVal = self.dfs(treeNode.right, result)
            if not isRightUniVal or treeNode.val != treeNode.right.val:
                amIUniVal = False
        if amIUniVal:
            result[0] += 1
        return amIUniVal

    def countUnivalSubtrees1(self, root: TreeNode) -> int:
        if root is None:
            return 0
        count = 0
        return self.dfs1(root, count)[1]

    def dfs1(self, treeNode: TreeNode, count: int) -> Tuple[bool, int]:
        if treeNode.left is None and treeNode.right is None:  # leaf
            count += 1
            return True, count  # leaf is always unival
        amIUniVal = True
        if treeNode.left is not None:
            isLeftUniVal, count = self.dfs1(treeNode.left, count)
            if not isLeftUniVal or treeNode.val != treeNode.left.val:
                amIUniVal = False

        if treeNode.right is not None:
            isRightUniVal, count = self.dfs1(treeNode.right, count)
            if not isRightUniVal or treeNode.val != treeNode.right.val:
                amIUniVal = False
        if amIUniVal:
            count += 1
        return amIUniVal, count


# Unit Tests


class TestCountUnivalSubtrees(unittest.TestCase):
    def testCountUnivalSubtrees1(self):
        root = TreeNode(5, TreeNode(1, TreeNode(5), TreeNode(5)),
                        TreeNode(5, None, TreeNode(5)))
        func = Solution().countUnivalSubtrees
        func2 = Solution().countUnivalSubtrees1
        self.assertEqual(func(root=root), 4)
        self.assertEqual(func2(root=root), 4)


if __name__ == "__main__":
    unittest.main()
