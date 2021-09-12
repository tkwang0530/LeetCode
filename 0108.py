"""
108. Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example1:
Given the sorted array: [-10, -3, 0, 5, 9]
One possible answer is: [0, -3, 9, -10, null, 5]
        0
      /    \
    -3     9
    /       /
-10     5  
"""

"""
Note:
1. Tree Construction - Top Down: O(n) time | O(logn) space
use binary search concept
2. Iteration: O(n) time | O(logn) space
"""




from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildTree(nums, 0, len(nums) - 1)
    
    def buildTree(self, nums, start, end) -> TreeNode:
        if start > end:
            return None
        mid = start + (end - start) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildTree(nums, start, mid - 1)
        root.right = self.buildTree(nums, mid + 1, end)
        return root

    def sortedArrayToBST2(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root = TreeNode(0)
        stack = [(root, 0, len(nums) - 1)] # (node, leftIndex, rightIndex)
        while len(stack) > 0:
            node, left, right = stack.pop()
            mid = left + (right - left) // 2
            node.val = nums[mid]
            if left < mid:
                node.left = TreeNode(0)
                stack.append((node.left, left, mid - 1))
            if mid < right:
                node.right = TreeNode(0)
                stack.append((node.right, mid+1, right))
        return root



# Unit Tests
import unittest
funcs = [Solution().sortedArrayToBST, Solution().sortedArrayToBST2]

class TestSortedArrayToBst(unittest.TestCase):
    def testSortedArrayToBst1(self):
        for func in funcs:
            nums = [-10, -3, 0, 5, 9]
            self.assertEqual(func(nums=nums).val, 0)
            self.assertEqual(func(nums=nums).left.val, -10)
            self.assertEqual(func(nums=nums).left.right.val, -3)
            self.assertEqual(func(nums=nums).right.val, 5)
            self.assertEqual(func(nums=nums).right.right.val, 9)


if __name__ == "__main__":
    unittest.main()
