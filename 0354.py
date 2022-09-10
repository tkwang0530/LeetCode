"""
354. Russian Doll Envelope
You are given a 2D array of integers envelopes where envelopes[i] = [w_i, h_i] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Constraints:
1 <= envelopes.length <= 10^5
envelopes[i].length == 2
1 <= w_i, h_i <= 10^5
"""

"""
Note:
1. Sort + DP(LIS): O(n^2) time | O(n) space - where n is the length of array envelopes
2. DP(LIS) + Greedy + Binary Search: O(nlogn) time | O(n) space - where n is the length of array envelopes
"""




import bisect
import unittest
from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        maxVal = 0
        dp = [0] * len(envelopes)
        for i in range(len(envelopes)-1, -1, -1):
            val = 0
            for j in range(i+1, len(envelopes)):
                if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
                    val = max(val, dp[j])
            dp[i] = val + 1
            maxVal = max(maxVal, dp[i])
        return maxVal

    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []

        # envelopes = [[2,3],[5,4],[6,7],[6,4]]
        # dp = [3, 4, 7]
        for _, height in envelopes:
            idx = bisect.bisect_left(dp, height)
            if idx == len(dp):
                dp.append(height)
            else:
                dp[idx] = height
        return len(dp)


# Unit Tests
funcs = [Solution().maxEnvelopes, Solution().maxEnvelopes2]


class TestMaxEnvelopes(unittest.TestCase):
    def testMaxEnvelopes1(self):
        for func in funcs:
            envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
            self.assertEqual(func(envelopes=envelopes), 3)

    def testMaxEnvelopes2(self):
        for func in funcs:
            envelopes = [[1, 1], [1, 1], [1, 1]]
            self.assertEqual(func(envelopes=envelopes), 1)

    def testMaxEnvelopes3(self):
        for func in funcs:
            envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
            self.assertEqual(func(envelopes=envelopes), 4)


if __name__ == "__main__":
    unittest.main()
