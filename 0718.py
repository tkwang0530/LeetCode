"""
718. Maximum Length of Repeated Subarray
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""

""" 
1. LCS: O(mn) time | O(mn) space
2. Binary Search + Rolling Hash: O((m+n)*log(min(m,n))) time | O(min(m+n))
"""

import collections
from typing import List
class Solution(object):
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) > len(nums1):
            nums2, nums1 = nums1, nums2
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        maxLength = 0
        for row in range(1, len(nums1)+1):
            for col in range(1, len(nums2)+1):
                num1 = nums1[row-1]
                num2 = nums2[col-1]
                if num1 == num2:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = 0
                maxLength = max(maxLength, dp[row][col])
        return maxLength

    def findLength2(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 1e9 + 7
        a = 101
        n1, n2 = len(nums1), len(nums2)
        power = [1] * (min(n1, n2)+1)
        for i in range(1, min(n1, n2)+1):
            power[i] = (power[i-1] * a) % MOD
        
        def search(L: int) -> int:
            h1 = h2 = 0

            # calculate the initial window hash value
            for i in range(L):
                h1 = (h1 * a + nums1[i]) % MOD
                h2 = (h2 * a + nums2[i]) % MOD

            # hashStartIndice about nums1
            hashStartIndice = collections.defaultdict(list)
            hashStartIndice[h1].append(0)
            for start in range(1, n1-L+1):
                h1 = h1 * a  # move window
                h1 = (h1 - nums1[start - 1] * power[L] % MOD + MOD) % MOD  # remove tail digit
                h1 = (h1 + nums1[start + L - 1]) % MOD # add new head digit
                hashStartIndice[h1].append(start)

            for i in hashStartIndice[h2]:
                    if nums1[i:i+L] == nums2[:L]:
                        return True
            for start in range(1, n2-L+1):
                h2 = h2 * a  # move window
                h2 = (h2 - nums2[start - 1] * power[L] % MOD + MOD) % MOD  # remove tail digit
                h2 = (h2 + nums2[start + L - 1]) % MOD # add new head digit
                for i in hashStartIndice[h2]:
                    if nums1[i:i+L] == nums2[start:start+L]:
                        return True
            return False

        left, right = 1, min(n1, n2) + 1
        maxLen = 0
        while left < right:
            mid = left + (right - left) // 2
            if search(mid):
                left = mid + 1
                maxLen = mid
            else:
                right = mid
        return maxLen

# Unit Tests
import unittest
funcs = [Solution().findLength, Solution().findLength2]

class TestFindLength(unittest.TestCase):
    def testFindLength1(self):
        for func in funcs:
            nums1 = [1,2,3,2,1]
            nums2 = [3,2,1,4,7]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 3)

    def testFindLength2(self):
        for func in funcs:
            nums1 = [0,0,0,0,0]
            nums2 = [0,0,0,0,0]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 5)

    def testFindLength3(self):
        for func in funcs:
            nums1 = [1,2,3,2,1]
            nums2 = [3,2,1,4]
            self.assertEqual(func(nums1=nums1, nums2=nums2), 3)

if __name__ == "__main__":
    unittest.main()
