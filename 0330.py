"""
330. Patching Array
description: https://leetcode.com/problems/patching-array/description/
"""

"""
Note:
1. Greedy: O(n) time | O(1) space
ref: https://leetcode.com/problems/patching-array/solutions/78488/solution-explanation
"""

from  typing import List
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        added = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added

# Unit Tests
import unittest
funcs = [Solution().minPatches]
class TestMinPatches(unittest.TestCase):
    def testMinPatches1(self):
        for func in funcs:
            nums = [1,3]
            n = 6
            self.assertEqual(func(nums, n), 1)


    def testMinPatches2(self):
        for func in funcs:
            nums = [1,5,10]
            n = 20
            self.assertEqual(func(nums, n), 2)


    def testMinPatches3(self):
        for func in funcs:
            nums = [1,2,2]
            n = 5
            self.assertEqual(func(nums, n), 0)


if __name__ == "__main__":
    unittest.main()
