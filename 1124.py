"""
1124. Longest Well-Performing Interval
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

Example1:
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].

Example2:
Input: hours = [6,6,6]
Output: 0

Constraints:
1 <= hours.length <= 10^4
0 <= hours[i] <= 16
"""

"""
Note:
1. PreSum + HashTable: O(n) time | O(n) space
"""

from  typing import List
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        preSums = [0] * (n+1) # preSums[i] means the total difference (tiring days - non-tiring days) from day_0 to day_i
        for i in range(1, n+1):
            if hours[i-1] > 8:
                preSums[i] = preSums[i-1] + 1
            else:
                preSums[i] = preSums[i-1] - 1

        longest = 0
        diffMinIndex = {0: 0}
        for i in range(1, n+1):
            diff = preSums[i]
            if diff > 0:
                longest = max(longest, i)
            elif diff - 1 in diffMinIndex:
                # diff - x also works, but it comes later than score - 1.
                # so the maximum interval is i - diffMinIndex[diff-1]
                longest = max(longest, i - diffMinIndex[diff - 1])
            
            if diff not in diffMinIndex:
                diffMinIndex[diff] = i
        return longest
# Unit Tests
import unittest
funcs = [Solution().longestWPI]


class TestLongestWPI(unittest.TestCase):
    def testLongestWPI1(self):
        for func in funcs:
            hours = [9,9,6,0,6,6,9]
            self.assertEqual(func(hours=hours), 3)

    def testLongestWPI2(self):
        for func in funcs:
            hours = [6,6,6]
            self.assertEqual(func(hours=hours), 0)

if __name__ == "__main__":
    unittest.main()
