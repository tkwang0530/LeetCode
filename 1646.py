"""
1646. Get Maximum in Generated Array
description: https://leetcode.com/problems/get-maximum-in-generated-array/description/
"""

"""
Note:
1. Simulation: O(n) time | O(n) space
"""

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n+1)
        nums[1] = 1
        
        maxNum = 1
        for i in range(2, n+1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]

            maxNum = max(maxNum, nums[i])

        return maxNum

# Unit Tests
import unittest
funcs = [Solution().getMaximumGenerated]


class TestGetMaximumGenerated(unittest.TestCase):
    def testGetMaximumGenerated1(self):
        for func in funcs:
            n = 7
            self.assertEqual(func(n=n), 3)

    def testGetMaximumGenerated2(self):
        for func in funcs:
            n = 2
            self.assertEqual(func(n=n), 1)

    def testGetMaximumGenerated3(self):
        for func in funcs:
            n = 3
            self.assertEqual(func(n=n), 2)

if __name__ == "__main__":
    unittest.main()
