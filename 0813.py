"""
813. Largest Sum of Averages
You are given an integer array nums and an integer k. You can partition the array into at most k non-empty adjacent subarrays. The score of a partition is the sum of the averages of each subarray.

Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

Return the maximum score you can achieve of all the possible partitions.
Answers within 10^-6 of the actual answer will be accepted.

Example1:
Input: nums = [9,1,2,3,9], k = 3
Output: 20.00000
Explanation: 
The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

Example2:
Input: nums = [1,2,3,4,5,6,7], k = 4
Output: 20.50000

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

"""
Note:
1. max recursion: O(n^2*k) time | O(nk) space
2. dp: O(n^2*k) time | O(nk) space
2. dp (improved): O(n^2*k) time | O(n) space
"""

from typing import List
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]
        
        memo = {}
        def dfs(i, tempK):
            if i == n:
                return 0
            if (i, tempK) in memo:
                return memo[(i, tempK)]
            if tempK == 1:
                return (preSums[n] - preSums[i]) / (n-1-i+1)

            maxSum = 0
            for j in range(i, n):
                maxSum = max(maxSum, (preSums[j+1] - preSums[i]) / (j-i+1) + dfs(j+1, tempK-1))
            memo[(i, tempK)] = maxSum
            return memo[(i, tempK)]
        return dfs(0, k)

    def largestSumOfAverages2(self, nums: List[int], k: int) -> float:
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]
        
        dp = [[0] * (n+1) for _ in range(k+1)]
        for tempK in range(1, k+1):
            for i in range(n-1, -1, -1):
                if tempK == 1:
                    dp[tempK][i] = (preSums[n] - preSums[i]) / (n-1-i+1)
                else:
                    dp[tempK][i] = max([(preSums[j+1] - preSums[i]) / (j-i+1) + dp[tempK-1][j+1] for j in range(i, n)])
        return dp[k][0]

    def largestSumOfAverages3(self, nums: List[int], k: int) -> float:
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]
        
        dp0 = [0] * (n+1)
        for tempK in range(1, k+1):
            dp1 = [0] * (n+1)
            for i in range(n-1, -1, -1):
                if tempK == 1:
                    dp1[i] = (preSums[n] - preSums[i]) / (n-1-i+1)
                else:
                    dp1[i] = max([(preSums[j+1] - preSums[i]) / (j-i+1) + dp0[j+1] for j in range(i, n)])
            dp0 = dp1
        return dp0[0]
            

# Unit Tests
import unittest
funcs = [Solution().largestSumOfAverages, Solution().largestSumOfAverages2, Solution().largestSumOfAverages3]

class TestLargestSumOfAverages(unittest.TestCase):
    def testLargestSumOfAverages1(self):
        for func in funcs:
            nums = [9,1,2,3,9]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 20.0)

    def testLargestSumOfAverages2(self):
        for func in funcs:
            nums = [1,2,3,4,5,6,7]
            k = 4
            self.assertEqual(func(nums=nums, k=k), 20.5)

    def testLargestSumOfAverages3(self):
        for func in funcs:
            nums = [4,1,7,5,6,2,3]
            k = 4
            self.assertTrue(abs(func(nums=nums, k=k) - 18.16667))

if __name__ == "__main__":
    unittest.main()