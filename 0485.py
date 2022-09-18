"""
485. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""

"""
Note:
1. Brute-Force: O(n) time | O(1) space - where n is the length of array nums
"""




from typing import List
import unittest
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for num in nums:
            if num == 0:
                count = 0
                continue

            count += 1
            maxCount = max(maxCount, count)
        return maxCount


# Unit Tests
funcs = [Solution().findMaxConsecutiveOnes]


class TestFindMaxConsecutiveOnes(unittest.TestCase):
    def testFindMaxConsecutiveOnes1(self):
        for func in funcs:
            nums = [1, 1, 0, 1, 1, 1]
            self.assertEqual(func(nums=nums), 3)

    def testFindMaxConsecutiveOnes2(self):
        for func in funcs:
            nums = [1, 0, 1, 1, 0, 1]
            self.assertEqual(func(nums=nums), 2)


if __name__ == "__main__":
    unittest.main()
