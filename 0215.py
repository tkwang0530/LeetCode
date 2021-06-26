"""
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Example1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example2:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""

"""
Note:
1. Sort and constant time lookup at index len(arr) - k: O(nlogn) time | O(1) space
2. Min Heap: O(nlogn) time | O(k) = O(n) space (no solution)
3. Quick sort: O(n) time | O(1) space
Best case: O(n)
Average case: O(n)
Worst case: O(n^2)
"""




import unittest
from typing import List
class Solution(object):
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        self.helper(nums, 0, len(nums) - 1, len(nums) - k)
        return nums[len(nums) - k]

    def partition(self, arr: List[int], left: int, right: int) -> int:
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] < pivot:
                self.swap(arr, i, j)
                i += 1
        self.swap(arr, i, right)  # put pivot at middle
        return i  # pivot index

    def helper(self, arr, left, right, k):
        if left == right:
            return
        pivot_index = self.partition(arr, left, right)
        if pivot_index == k:
            return
        elif k < pivot_index:
            self.helper(arr, left, pivot_index - 1, k)  # LHS
        else:
            self.helper(arr, pivot_index + 1, right, k)  # RHS

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


        # Unit Tests
funcs = [Solution().findKthLargest, Solution().findKthLargest2]


class TestFindKthLargest(unittest.TestCase):
    def testFindKthLargest1(self):
        for func in funcs:
            nums = [3, 2, 1, 5, 6, 4]
            k = 2
            self.assertEqual(
                func(nums=nums, k=k), 5)

    def testFindKthLargest2(self):
        for func in funcs:
            nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
            k = 4
            self.assertEqual(
                func(nums=nums, k=k), 4)


if __name__ == "__main__":
    unittest.main()
