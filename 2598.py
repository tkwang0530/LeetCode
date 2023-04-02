"""
2598. Smallest Missing Non-negative Integer After Operations
You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

Example1:
Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.

Example2:
Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
Explanation: One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve.

Constraints:
1 <= nums.length, value <= 10^5
-10^9 <= nums[i] <= 10^9
"""

"""
Note:
1. HashTable: O(n) time | O(value) space - where n is the length of array nums and value
"""




import unittest
from typing import List
import collections
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        remainderCount = collections.defaultdict(int)
        for num in nums:
            remainderCount[num % value] += 1

        mex = 0
        for i in range(n):
            remainder = i % value
            if remainderCount[remainder] > 0:
                mex += 1
                remainderCount[remainder] -= 1
            else:
                return mex
        return mex


# Unit Tests
funcs = [Solution().findSmallestInteger]


class TestFindSmallestInteger(unittest.TestCase):
    def testFindSmallestInteger1(self):
        for func in funcs:
            nums = [1, -10, 7, 13, 6, 8]
            value = 5
            self.assertEqual(func(nums=nums, value=value), 4)

    def testFindSmallestInteger2(self):
        for func in funcs:
            nums = [1, -10, 7, 13, 6, 8]
            value = 7
            self.assertEqual(func(nums=nums, value=value), 2)


if __name__ == "__main__":
    unittest.main()
