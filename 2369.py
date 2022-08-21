"""
2369. Check if There is a Valid Partition For The Array
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:
1. The subarrays consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
2. The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
3. The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.

Return true if the array has at least one valid partition. Otherwise, return false.

Example1:
Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.

Example2:
Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.

Constraints:
2 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""

"""
Note:
1. dfs+memo: O(n) time | O(n) space
2. dp: O(n) time | O(1) space
"""

from typing import List
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        def isValid(nums, i, j):
            if j >= len(nums):
                return False
            if j - i == 1:
                return nums[i] == nums[j]
            
            if j - i == 2:
                return (nums[i] == nums[i+1] == nums[i+2]) or ((nums[i+1] == nums[i]+1) and (nums[i+2] == (nums[i+1]+1)))
        
        n = len(nums)
        memo = {}
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            left = n - idx
            if left == 2:
                return isValid(nums, idx, idx+1)
            elif left == 3:
                return isValid(nums, idx, idx+2)
            elif left == 1:
                return False
            elif left == 0:
                return True
            elif left > 3:
                ans = False
                ans |= isValid(nums, idx, idx+2) and dfs(idx+3)
                ans |= isValid(nums, idx, idx+1) and dfs(idx+2)
                memo[idx] = ans
            return memo[idx]
        return dfs(0)

    def validPartition2(self, nums: List[int]) -> bool:
        n = len(nums)
        def isValid(nums, i, j):
            if j >= len(nums):
                return False
            if j - i == 1:
                return nums[i] == nums[j]
            
            if j - i == 2:
                return (nums[i] == nums[i+1] == nums[i+2]) or ((nums[i+1] == nums[i]+1) and (nums[i+2] == (nums[i+1]+1)))

        dp = [False, True, True] # initialize ans for index n-1, n+1, n+2
        for i in range(n-2, -1, -1):
            next = False
            next |= isValid(nums, i, i+1) and dp[1]
            next |= isValid(nums, i, i+2) and dp[2]
            dp[0], dp[1], dp[2] = next, dp[0], dp[1]
        return dp[0]

# Unit Tests
import unittest
funcs = [Solution().validPartition, Solution().validPartition2]
class TestValidPartition(unittest.TestCase):
    def testValidPartition1(self):
        for func in funcs:
            nums = [4,4,4,5,6]
            self.assertEqual(func(nums=nums), True)

    def testValidPartition2(self):
        for func in funcs:
            nums = [1,1,1,2]
            self.assertEqual(func(nums=nums), False)

if __name__ == "__main__":
    unittest.main()
