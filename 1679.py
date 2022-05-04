"""
1679. Max Numbers of K-Sum Pairs
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9
"""

"""
Note:
1. HashTable: O(n) time | O(n) space
2. HashTable2: O(n) time | O(n) space
"""

from typing import List

import collections
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numCount = collections.Counter(nums)
        result = 0
        for num, count in numCount.items():
            result += min(count, numCount.get(k-num, 0))

        return result // 2

    def maxOperations2(self, nums: List[int], k: int) -> int:
        numCount = collections.Counter(nums)
        return sum(min(count, numCount.get(k-num, 0)) for num, count in numCount.items()) // 2

# Unit Tests
import unittest
funcs = [Solution().maxOperations, Solution().maxOperations2]

class TestMaxOperations(unittest.TestCase):
    def testMaxOperations1(self):
        for func in funcs:
            nums = [1,2,3,4]
            k = 5
            self.assertEqual(func(nums=nums, k=k), 2)

    def testMaxOperations2(self):
        for func in funcs:
            nums = [3,1,3,4,3]
            k = 6
            self.assertEqual(func(nums=nums, k=k), 1)

if __name__ == "__main__":
    unittest.main()