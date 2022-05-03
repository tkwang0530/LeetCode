"""
581. Shortest Unsorted Continuous Subarray
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.


Example2:
Input: nums = [1,2,3,4]
Output: 0

Example3:
Input: nums = [1]
Output: 0

Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5

Follow up: Can you solve it in O(n) time complexity?
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space
(1) increase left and decrease right if possible
(2) find the lowest and largest value between left and right
(3) extend subarray by the stored lowest and largest values

2. Monotonic Stacks: O(n) time | O(n) space
"""

import unittest
from  typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right and nums[left] <= nums[left + 1]:
            left += 1
        while left < right and nums[right] >= nums[right-1]:
            right -= 1
        if left == right:
            return 0
        minOfSubarray = float("inf")
        maxOfSubarray = float("-inf")
        for i in range(left, right + 1):
            minOfSubarray = min(minOfSubarray, nums[i])
            maxOfSubarray = max(maxOfSubarray, nums[i])
        
        while left > 0 and nums[left-1] > minOfSubarray:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] < maxOfSubarray:
            right += 1
        return right - left + 1

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        start, end = len(nums), 0
        
        # e.g. [2,6,4,8,10,9,15]
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end, stack.pop())
            stack.append(i)

        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start, stack.pop())
            stack.append(i)
        return end - start + 1 if end != 0 else 0

# Unit Tests
funcs = [Solution().findUnsortedSubarray, Solution().findUnsortedSubarray2]


class TestFindUnsortedSubarray(unittest.TestCase):
    def testFindUnsortedSubarray1(self):
        for func in funcs:
            nums = [2,6,4,8,10,9,15]
            self.assertEqual(
                func(nums=nums), 5)

    def testFindUnsortedSubarray2(self):
        for func in funcs:
            nums = [1,2,3,4]
            self.assertEqual(
                func(nums=nums), 0)

    def testFindUnsortedSubarray3(self):
        for func in funcs:
            nums = [1]
            self.assertEqual(
                func(nums=nums), 0)

if __name__ == "__main__":
    unittest.main()
