"""
1144. Decrease Elements To Make Array Zigzag
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:
- Every even-indexed element is greater than adjacent elements, i.e. A[0] > A[1] < A[2] > A[3] < A[4] > ...
- Every odd-indexed element is greater than adjacent elements, i.e. A[0] < A[1] > A[2] < A[3] > A[4] < ...

Example1:
Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.

Example2:
Input: nums = [9,6,1,6,2]
Output: 4

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""

"""
Note:
1. Two Pass: O(n) time | O(1) space
"""

from typing import List
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        largeFirstMoves = 0
        
        i = 1
        while i < n:
            curr = nums[i]
            prev = nums[i-1] if i-1 >= 0 else float("inf")
            next = nums[i+1] if i+1 < n else float("inf")
            minVal = min(prev, next)
            if curr >= minVal:
                largeFirstMoves += curr - minVal + 1
            i += 2
        
        smallFirstMoves = 0
        i = 0
        while i < n:
            curr = nums[i]
            prev = nums[i-1] if i-1 >= 0 else float("inf")
            next = nums[i+1] if i+1 < n else float("inf")
            minVal = min(prev, next)
            if curr >= minVal:
                smallFirstMoves += curr - minVal + 1
            i += 2
        
        return min(smallFirstMoves, largeFirstMoves)


# Unit Tests
import unittest
funcs = [Solution().movesToMakeZigzag]
class TestMovesToMakeZigzag(unittest.TestCase):
    def testMovesToMakeZigzag1(self):
        for func in funcs:
            nums = [1,2,3]
            self.assertEqual(func(nums=nums), 2)

    def testMovesToMakeZigzag2(self):
        for func in funcs:
            nums = [9,6,1,6,2]
            self.assertEqual(func(nums=nums), 4)


if __name__ == "__main__":
    unittest.main()
