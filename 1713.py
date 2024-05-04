"""
1713. Minimum Operations to Make a Subsequence
description: https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/description/
"""

"""
Note:
1. LCS (TLE): O(mn) time | O(min(m, n)) space - where m is  length of array target and n is the length of array arr
2. Reduce to LIS: O(nlogm) time | O(2m) space - where m is the length of array target and n is the length of array arr
Key: numbers in target are distinct
    1. Ignore numbers that are not in target
    2. Convert numbers to indices
ex:
    target = [6,4,8,1,3,2] => [0,1,2,3,4,5] -> [0,2,3]
    arr = [4,7,6,2,3,8,6,1] => [1,0,5,4,2,0,3] -> [0,2,3]

ref: https://www.youtube.com/watch?v=5vBPESNPEu4
"""

import bisect
class Solution:
    def minOperations(self, target, arr):
        m, n = len(target), len(arr)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1],
                    dp[i-1][j-1] + (target[i-1] == arr[j-1])
                )
        return m - dp[m][n]

class Solution2:
    def minOperations(self, target, arr):
        def LIS(nums: list[int]) -> int:
            dp = []
            for num in nums:
                if not dp or num > dp[-1]:
                    dp.append(num)
                else:
                    dp[bisect.bisect_left(dp, num)] = num
            return len(dp)
        
        numIndex = {num: i for i, num in enumerate(target)}
        nums = [numIndex[num] for num in arr if num in numIndex]
        return len(target) - LIS(nums)


# Unit Tests
import unittest
funcs = [Solution().minOperations, Solution2().minOperations]
class TestMinOperations(unittest.TestCase):
    def test_MinOperations1(self):
        for func in funcs:
            target = [5,1,3]
            arr = [9,4,2,3,4]
            self.assertEqual(func(target=target, arr=arr), 2)

    def test_MinOperations2(self):
        for func in funcs:
            target = [6,4,8,1,3,2]
            arr = [4,7,6,2,3,8,6,1]
            self.assertEqual(func(target=target, arr=arr), 3)

if __name__ == "__main__":
    unittest.main()
