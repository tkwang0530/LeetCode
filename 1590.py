"""
1590. Make Sum Divisible by P
description: https://leetcode.com/problems/make-sum-divisible-by-p/description/
"""

"""
Note:
1. PreSum + HashTable: O(n) time | O(n) space - where n is the length of array nums
ref: https://leetcode.com/problems/make-sum-divisible-by-p/solutions/854197/java-c-python-prefix-sum
"""

from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        removed = sum(nums) % p
        dp = {0: -1}
        current = 0
        res = n = len(nums)
        for i, num in enumerate(nums):
            current = (current + num) % p
            dp[current] = i
            if (current - removed) % p in dp:
                res = min(res, i - dp[(current - removed) % p])
        return res if res < n else -1

funcs = [Solution().minSubarray]

import unittest
class TestMinSubarray(unittest.TestCase):
    def testMinSubarray1(self):
        for func in funcs:
            nums = [3,1,4,2]
            p = 6
            self.assertEqual(func(nums=nums, p=p), 1)

    def testMinSubarray2(self):
        for func in funcs:
            nums = [6,3,5,2]
            p = 9
            self.assertEqual(func(nums=nums, p=p), 2)

    def testMinSubarray3(self):
        for func in funcs:
            nums = [1,2,3]
            p = 3
            self.assertEqual(func(nums=nums, p=p), 0)

if __name__ == "__main__":
    unittest.main()
