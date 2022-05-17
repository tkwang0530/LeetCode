"""
560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example1:
Input: nums = [1,1,1], k = 2
Output: 2

Example2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""

"""
Note:
1. HashTable + PreSum: O(n) time | O(n) space
<subarraySum, count>
2. Brute Force: O(n^2) time | O(1) space
"""

import unittest
from  typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currSum = 0
        prefixSums = {0: 1}
        for num in nums:
            currSum += num
            diff = currSum - k
            result += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        return result

    def subarraySum2(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                if currSum == k:
                    result += 1
        return result


# Unit Tests
funcs = [Solution().subarraySum, Solution().subarraySum2]


class TestSubarraySum(unittest.TestCase):
    def testSubarraySum1(self):
        for func in funcs:
            nums = [1, 1, 1]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 2)

    def testSubarraySum2(self):
        for func in funcs:
            nums = [1, 2, 3]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 2)


if __name__ == "__main__":
    unittest.main()
