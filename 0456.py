"""
456. 132 Pattern
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j]

Return true if there is a 132 pattern in nums, otherwise, return false.

Example1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

Constraints:
n == nums.length
1 <= n <= 2 * 10^5
-10^9 <= nums[i] <= 10^9
"""

"""
Note:
1. PreMins + Stack: O(n) time | O(1) space
"""

import unittest
from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        n = len(nums)

        preMins = [-1] * n
        preMins[0] = nums[0]
        for i in range(1, n):
            preMins[i] = min(preMins[i-1], nums[i])
        
        # use stack to stores candidate nums[k], statisfying nums[k] > preMins[j-1]
        stack = []
        for j in range(n-1, 0, -1):
            if nums[j] <= preMins[j-1]:
                continue

            # from now on, we ensure that there are at least one nums[i] < nums[j], where i < j

            # pop out invalid nums[k] from the stack
            while stack and stack[-1] <= preMins[j-1]:
                stack.pop()

            if stack and stack[-1] < nums[j]:
                return True
            
            stack.append(nums[j])
        
        return False

# Unit Tests
funcs = [Solution().find132pattern]


class TestFind132pattern(unittest.TestCase):
    def testFind132pattern1(self):
        for func in funcs:
            nums = [1,2,3,4]
            self.assertEqual(func(nums=nums), False)

    def testFind132pattern2(self):
        for func in funcs:
            nums = [3,1,4,2]
            self.assertEqual(func(nums=nums), True)

    def testFind132pattern3(self):
        for func in funcs:
            nums = [-1,3,2,0]
            self.assertEqual(func(nums=nums), True)


if __name__ == "__main__":
    unittest.main()
