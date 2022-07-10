"""
1014. Best Sightseeing Pair
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example1:
Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

Example2:
Input: values = [1,2]
Output: 2

Constraints:
2 <= values.length <= 5 * 10^4
1 <= values[i] <= 1000
"""

"""
Note:
1. SuffixMax: O(n) time | O(n) space - where n is the length of values
(1) values[i] + values[j] + i - j = (values[i]+i) + (values[j]-j)
(2) Build a SuffixMax array
(3) iterate each number, and get the Max values[j]-j from position i, and update the target
"""

from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        plus = [0] * n
        minus = [0] * n
        for i in range(n):
            plus[i] = values[i]+i
            minus[i] = values[i]-i

        suffixMinusMax = [-float("inf")] * n
        suffixMinusMax[-1] = minus[-1]
        for i in range(n-2, -1, -1):
            suffixMinusMax[i] = max(suffixMinusMax[i+1], minus[i])

        maxVal = -float("inf")
        for i in range(n-1):
            maxVal = max(maxVal, plus[i]+suffixMinusMax[i+1])
        return maxVal
        
# Unit Tests
import unittest
funcs = [Solution().maxScoreSightseeingPair]
class TestMaxScoreSightseeingPair(unittest.TestCase):
    def testMaxScoreSightseeingPair1(self):
        for func in funcs:
            values = [8,1,5,2,6]
            self.assertEqual(func(values=values), 11)

    def testMaxScoreSightseeingPair2(self):
        for func in funcs:
            values = [1,2]
            self.assertEqual(func(values=values), 2)

if __name__ == "__main__":
    unittest.main()
