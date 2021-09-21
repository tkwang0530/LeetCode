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
1. Sort and constant time lookup at index len(arr) - k: O(nlogn) time | O(n) space
2. Min Heap: O(nlogk) time | O(k)
3. Quick Select: O(n) time | O(logn) space
Best case: O(n)
Average case: O(n)
Worst case: O(n^2)
"""




import unittest
from typing import List
from heapq import heappop, heappush, heappushpop
class Solution(object):
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            if len(minHeap) < k:
                heappush(minHeap, num)
            else:
                heappushpop(minHeap, num)
        return heappop(minHeap)

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        self.helper(nums, 0, len(nums) - 1, len(nums) - k)
        return nums[len(nums) - k]
    
    def helper(self, nums, left, right, targetIndex) -> None:
        if left == right:
            return
        pivotIndex = self.partition(nums, left, right)
        if pivotIndex == targetIndex:
            return
        elif pivotIndex > targetIndex:
            self.helper(nums, left, pivotIndex - 1, targetIndex)
        else:
            self.helper(nums, pivotIndex + 1, right, targetIndex)
    
    def partition(self, nums, left, right) -> int:
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i


        # Unit Tests
funcs = [Solution().findKthLargest, Solution().findKthLargest2, Solution().findKthLargest3]


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
