"""
1004. Max Consecutive Ones III
Given an array A of 0s and 1s, we may change up to k values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.
Examples:
    Input: A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2
    Output: 6

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

"""
Note:
1. Brute Force: O(n^2) time | O(1) space
2. Sliding Window: O(n) time | O(1) space
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        longest = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            while k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            longest = max(longest, j - i + 1)
        return longest


# Unit Tests
import unittest


class TestLongestOnes(unittest.TestCase):
    def testLongestOnes1(self):
        func = Solution().longestOnes
        self.assertEqual(func(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2), 6)

    def testLongestOnes2(self):
        func = Solution().longestOnes
        self.assertEqual(
            func(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3),
            10,
        )


if __name__ == "__main__":
    unittest.main()