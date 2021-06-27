"""
230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Example1:
        3
      /    \
    1       4
       \
        2

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example2:
                        5
                    /       \
                  3         6
                /    \
             2        4
           /
        1
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

"""
Note:
1. Iterative solution: O(n) time | O(n) space
2. Recursive solution: O(n) time | O(n) space
"""




from typing import List, Tuple
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root is not None or len(stack) > 0:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                break
            root = root.right
        return root.val

    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        result = [0, k]  # [result, current k]
        self.dfs(root, k, result)
        return result[0]

    def dfs(self, root: TreeNode, k: int, result: List[int]):
        if root.left is not None:
            self.dfs(root.left, k, result)

        if result[1] == 0:
            return
        result[1] -= 1
        result[0] = root.val

        if root.right is not None:
            self.dfs(root.right, k, result)


# Unit Tests
funcs = [Solution().kthSmallest, Solution().kthSmallest2]


class TestKthSmallestl(unittest.TestCase):
    def testKthSmallestl1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
            self.assertEqual(func(root=root, k=1), 1)

    def testKthSmallestl2(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(3, TreeNode(
                2, TreeNode(1)), TreeNode(4)), TreeNode(6))
            self.assertEqual(func(root=root, k=3), 3)


if __name__ == "__main__":
    unittest.main()
