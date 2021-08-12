"""
270. Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target

Note:
- Given target value is a floating point.
- You are guaranteed to have only one unique value in the BST that is closest to the target.

Example1:
        4
      /    \
    2       5
 /     \
1       3

Input: root = [4, 2, 5, 1, 3], target = 3.714286
Output: 4
"""

"""
Note:
1. Iterative (DFS inorder traversal): O(n) time | O(n) space
2. Iterative (Binary Search): O(h) time | O(1) space
3. Recursive (Binary Search): O(h) time | O(h) space
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack = []
        closest = float("inf")
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            root = root.right
        return closest

    def closestValue2(self, root: TreeNode, target: float) -> int:
        closest = float("inf")
        while root is not None:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val

            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            else:
                return root.val
        return closest

    def closestValue3(self, root: TreeNode, target: float) -> int:
        closest = [root.val]
        self.closestValueHelper(root, target, closest)
        return closest[0]

    def closestValueHelper(self, root: TreeNode, target: float, closest: List[int]) -> None:
        if abs(root.val - target) < abs(closest[0] - target):
            closest[0] = root.val

        if root.val < target and root.right:
            self.closestValueHelper(root.right, target, closest)

        if root.val > target and root.left:
            self.closestValueHelper(root.left, target, closest)


# Unit Tests
funcs = [Solution().closestValue, Solution().closestValue2,
         Solution().closestValue3]


class TestClosestValue(unittest.TestCase):
    def testClosestValue1(self):
        for func in funcs:
            root = TreeNode(4, TreeNode(
                2, TreeNode(1), TreeNode(3)), TreeNode(5))
            self.assertEqual(func(root=root, target=3.714286), 4)

    def testClosestValue2(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(
                4)), TreeNode(8, TreeNode(6), TreeNode(10)))
            self.assertEqual(func(root=root, target=5.789), 6)

    def testClosestValue3(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root, target=100), 1)


if __name__ == "__main__":
    unittest.main()
