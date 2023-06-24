"""
2012. Sum of Beauty in the Array
You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
0, if none of the previous conditions holds.
Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

Example1:
Input: nums = [1,2,3]
Output: 2
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.

Example2:
Input: nums = [2,4,6,4]
Output: 1
Explanation: For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.

Example3:
Input: nums = [3,2,1]
Output: 0
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.

Constraints:
3 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

"""
Note:
1. prefix + suffix: O(n) time | O(n) space - where n is the length of array nums
"""

import unittest
from typing import List
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        prefixMax = [-float("inf")] * n
        suffixMin = [float("inf")] * n
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i-1], nums[i-1])
        
        for i in range(n-2, -1, -1):
            suffixMin[i] = min(suffixMin[i+1], nums[i+1])
            
        total = 0
        for i in range(1, n-1):
            if prefixMax[i] < nums[i] < suffixMin[i]:
                total += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                total += 1
        return total

# Unit Tests
import unittest
funcs = [Solution().sumOfBeauties]
class TestSumOfBeauties(unittest.TestCase):
    def testSumOfBeauties1(self):
        for func in funcs:
            nums = [1,2,3]
            self.assertEqual(func(nums=nums), 2)

    def testSumOfBeauties2(self):
        for func in funcs:
            nums = [2,4,6,4]
            self.assertEqual(func(nums=nums), 1)

    def testSumOfBeauties3(self):
        for func in funcs:
            nums = [3,2,1]
            self.assertEqual(func(nums=nums), 0)

if __name__ == "__main__":
    unittest.main()
