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
Average case: O(logn)
Worst case: O(n)
"""

import random
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
        targetIndex = len(nums) - k
        def partition(nums, left, right) -> int:
            randInt = random.randint(left, right)
            nums[randInt], nums[right] = nums[right], nums[randInt]
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] < pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i
    
        def helper(nums, left, right) -> None:
            if left == right:
                return
            pivotIndex = partition(nums, left, right)
            if pivotIndex == targetIndex:
                return
            elif pivotIndex > targetIndex:
                helper(nums, left, pivotIndex - 1)
            else:
                helper(nums, pivotIndex + 1, right)
                
        helper(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]


# Unit Tests
import unittest
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
