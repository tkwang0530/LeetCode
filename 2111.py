"""
2111. Minimum Operations to Make the Array K-Increasing
description: https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/description/
"""

"""
Note:
1. LIS: O(k * (n/k)log(n/k)) time | O(n/k) space
"""

import bisect
from typing import List
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # return the longest increasing subsequence's length of the subarray starting from index 
        def LIS(i):
            dp = []
            for j in range(i, n, k):
                if not dp or dp[-1] <= arr[j]:
                    dp.append(arr[j])
                    continue
                idx = bisect.bisect_right(dp, arr[j])
                dp[idx] = arr[j]
            return len(dp)

        totalLIS = 0
        for head in range(k):
            totalLIS += LIS(head)
            
        return n - totalLIS
    
# Unit Tests
import unittest
funcs = [Solution().kIncreasing]


class TestKIncreasing(unittest.TestCase):
    def testKIncreasing1(self):
        for kIncreasing in funcs:
            arr = [5,4,3,2,1]
            k = 1
            self.assertEqual(kIncreasing(arr=arr, k=k), 4)

    def testKIncreasing2(self):
        for func in funcs:
            arr = [4,1,5,2,6,2]
            k = 2
            self.assertEqual(func(arr=arr, k=k), 0)

    def testKIncreasing3(self):
        for func in funcs:
            arr = [4,1,5,2,6,2]
            k = 3
            self.assertEqual(func(arr=arr, k=k), 2)

if __name__ == "__main__":
    unittest.main()
