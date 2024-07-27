"""
1043. Partition Array for Maximum Sum
description: https://leetcode.com/problems/partition-array-for-maximum-sum/description/
"""

"""
Note:
1. dp: O(n) time | O(n) space - where n is the length of array arr
"""

import unittest
from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        dp = [-float("inf")] * (n+1)
        dp[n] = 0
        for i in range(n-1, -1, -1):
            localMax = -float("inf")
            for j in range(i+1, n+1):
                if (j-i) > k:  
                    break
                localMax = max(localMax, arr[j-1])
                dp[i] = max(dp[i], (j-i) * localMax + dp[j])
        
        return dp[0]

# Unit Tests
funcs = [Solution().maxSumAfterPartitioning]

class TestMaxSumAfterPartitioning(unittest.TestCase):
    def testMaxSumAfterPartitioning1(self):
        for func in funcs:
            arr = [1,15,7,9,2,5,10]
            k = 3
            self.assertEqual(func(arr=arr, k=k), 84)

    def testMaxSumAfterPartitioning2(self):
        for func in funcs:
            arr = [1,4,1,5,7,3,6,1,9,9,3]
            k = 4
            self.assertEqual(func(arr=arr, k=k), 83)

    def testMaxSumAfterPartitioning3(self):
        for func in funcs:
            arr = [1]
            k = 1
            self.assertEqual(func(arr=arr, k=k), 1)



if __name__ == "__main__":
    unittest.main()
