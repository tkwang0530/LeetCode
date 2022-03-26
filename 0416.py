"""
416. Partition Equal Subset Sum
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

""" 
1. dp: O(2^n) time | O((2^n) ^ 2) space
2. dp(improved): O(2^n) time | O(2^n) space
"""

from typing import List
class Solution(object):
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        
        sumSets = [set() for _ in range(len(nums))]
        sumSets.append(set([0]))
        for i in range(len(nums) - 1, -1, -1):
            preSumSet = sumSets[i+1]
            sumSets[i] = sumSets[i+1].copy()
            for s in preSumSet:
                if s+nums[i] == totalSum // 2:
                    return True
                sumSets[i].add(s+nums[i])
        return False

    def canPartition2(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        
        preSumSet = set([0])
        for i in range(len(nums) - 1, -1, -1):
            currentSumSet = preSumSet.copy()
            for s in preSumSet:
                if s+nums[i] == totalSum // 2:
                    return True
                currentSumSet.add(s+nums[i])
            preSumSet = currentSumSet
        return False

# Unit Tests
import unittest
funcs = [Solution().canPartition, Solution().canPartition2]


class TestCanPartition(unittest.TestCase):
    def testCanPartition1(self):
        for func in funcs:
            nums = [1,5,11,5]
            self.assertEqual(func(nums=nums), True)

    def testCanPartition2(self):
        for func in funcs:
            nums = [1,2,3,5]
            self.assertEqual(func(nums=nums), False)

if __name__ == "__main__":
    unittest.main()
