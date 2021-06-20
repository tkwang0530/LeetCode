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
1. Tree Construction - Top Down: O(n) time | O(n) space
use binary search concept
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBst(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, arr, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(arr[start])
        mid = (start + end) // 2
        subtreeRoot = TreeNode(arr[mid])
        subtreeRoot.left = self.helper(arr, start, mid - 1)
        subtreeRoot.right = self.helper(arr, mid + 1, end)
        return subtreeRoot

# Unit Tests


class TestSortedArrayToBst(unittest.TestCase):
    def testSortedArrayToBst1(self):
        nums = [-10, -3, 0, 5, 9]
        func = Solution().sortedArrayToBst
        self.assertEqual(func(nums=nums).val, 0)
        self.assertEqual(func(nums=nums).left.val, -10)
        self.assertEqual(func(nums=nums).left.right.val, -3)
        self.assertEqual(func(nums=nums).right.val, 5)
        self.assertEqual(func(nums=nums).right.right.val, 9)


if __name__ == "__main__":
    unittest.main()
